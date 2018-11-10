import numpy as np
#from PlayFair import strToDiagraphs
def strToDiagraphs(plain_text):
    diagraph=[]
    for c in range((len(plain_text)//2)) :
        diagraph.append(plain_text[c*2:c*2+2])
    return diagraph
def strToRTrigraphs(plain_text):
    Trigraph=[]
    for c in range((len(plain_text)//3)) :
        Trigraph.append(plain_text[c*3:c*3+3])
    return Trigraph
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def srtToUpper(Text) :
    ret_str=""
    for i in range(len(Text)) :
       if(Text[i].isalpha()==True) :
        ret_str+=Text[i]
    return ret_str

def hill_cipher_2x2(plainText,matix_key):
    print(len(alpha))
    cipher_list=[]
    for str_txt in plainText :
        #append X if srting is odd

        print(str_txt)
        str_data = srtToUpper(str_txt)
        print(str_data)
        cipher_text=""
        if(len(str_data)%2 != 0) :
            str_data+='X'

        diags=strToDiagraphs(str_data)
        print(diags)
        for diag in diags:
            mat1= [alpha.find(diag[0]),alpha.find(diag[1])]
            mat_mult=np.matmul(matix_key,mat1)
            mat_mult=mat_mult % 26
            cipher_text+=alpha[mat_mult[0]]+alpha[mat_mult[1]]
        cipher_list.append(cipher_text+'\n')
        #print(mat_mult)
    return cipher_list

#hill_cipher(None,None)
def hill_cipher_3x3(plainText,matix_key):
    print(len(alpha))
    cipher_list=[]
    for str_txt in plainText :
        #append X if srting is odd

        print(str_txt)
        str_data = srtToUpper(str_txt)
        print(str_data)
        cipher_text=""
        if(len(str_data)%2 == 0) :
            str_data+='X'

        diags=strToRTrigraphs((str_data))
        print(diags)
        for diag in diags:
            print(diag)
            mat1 = [alpha.find(diag[0]),alpha.find(diag[1]),alpha.find(diag[2])]
            mat_mult = np.matmul(matix_key,mat1)
            mat_mult = mat_mult % 26
            cipher_text+=alpha[mat_mult[0]]+alpha[mat_mult[1]]+alpha[mat_mult[2]]
        cipher_list.append(cipher_text+'\n')
        #print(mat_mult)
    return cipher_list