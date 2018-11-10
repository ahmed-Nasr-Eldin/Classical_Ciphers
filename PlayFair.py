import copy
def formMatrix(key) :
    matrix=[]
    matrix_str=""

    for c in key.upper():
        if c not in matrix_str :
            matrix_str+=c
#complete the missing elements
    for index in range(65,91): #loop through alphapets
        if (chr(index).upper() not in matrix_str) and (chr(index) != 'J') :
            matrix_str+=(chr(index))
    for i in range(5):
        matrix.append(matrix_str[i*5:5+i*5])
    return matrix

#plain text came as list of strings
def str_filler(plain_text):
    plainModifiedStr=""
    for ch_r in range(len(plain_text)-1) :
        if(plain_text[ch_r].upper()==plain_text[ch_r+1].upper()):
            plainModifiedStr+=(plain_text[ch_r].upper())
            plainModifiedStr += 'X'
        else :
            plainModifiedStr+=(plain_text[ch_r].upper())
    plainModifiedStr += (plain_text[ch_r+1].upper())
    if ((len(plainModifiedStr) % 2) !=0 ) :    #number is not odd
        plainModifiedStr+='X'
    return plainModifiedStr
#def PfairAlgorithm(plain_text,key) : # key is string
    ############## modify the plain Text ############33
def strToDiagraphs(plain_text):
    diagraph=[]
    for c in range((len(plain_text)//2)) :
        diagraph.append(plain_text[c*2:c*2+2])
    return diagraph
def encode(matrix,plain_diagraphs):
    #locate each x and y of the matrix
    #if same row x+1 , if it exceeds wrap to the left
    #if same column y,y+1 next below
    #if in matrix opposite corners
    #x1,y1 and x2,y2 ------> x2,y1 and x1,y2
    cipher_text=""
    dic_x_y={}
    for diag in plain_diagraphs:
    #get x,y for diag
        y1=0
        y2=0
        x1=0
        x2=0
        for i in range(len(matrix)) :
            if((matrix[i].find(diag[0]))!=-1):
                x1 = matrix[i].find(diag[0])
                y1=i
            if ((matrix[i].find(diag[1])) != -1):
                x2 = matrix[i].find(diag[1])
                y2 = i
##########if same row  ######
        if y1 == y2 :
            cipher_text+=matrix[y1][(x1+1)%5]
            cipher_text+=matrix[y2][(x2+1)%5]
        elif x1 == x2:
            cipher_text += matrix[(y1+1)%5][x1]
            cipher_text += matrix[(y2+1)%5][x2]
        else :
            cipher_text +=matrix[y1][x2]
            cipher_text +=matrix[y2][x1]
    return cipher_text
#print(formMatrix('PLAYFAIREXAMPLE'))
#print(str_filler('Hidethegoldinthetreestump'))
#print(strToDiagraphs(str_filler('Hidethegoldinthetreestump')))
cipher=encode(formMatrix('PLAYFAIREXAMPLE'),strToDiagraphs(str_filler('Hidethegoldinthetreestump')))
######## Function takes a list of plain strings and return list of cipher strings ##################
############# it also take a string as key ###################


def play_fair(plain_list,key):
    matrix=formMatrix(key)
    cipher_list=[]
    for plain_str in plain_list :
        modified_str=str_filler(plain_str)
        diag=strToDiagraphs(modified_str)
        #append the Cipher text one after the other )
        cipher_txt=(encode(matrix,diag))
        cipher_list.append(cipher_txt+'\n')
        print(cipher_txt)
    print(cipher_list)
    return cipher_list

#print(cipher)
#gen= (c in key or i in range(25))
    # for i_n in range(5):  #in range of 5
    #     #matrix.append()             #add new row to matrix
    #     for i_k in range(len(key)): #finish the keyword
    #         if (i_k < 5):
    #             if(key[i_k] not in matrix_str):
    #                 matrix_str.append(key[i_k])
    #         else:
    #             i_n=i_n+1
    #             break
    #key generated