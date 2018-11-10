#from Hill import srtToUpper
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def srtToUpper(Text) :
    ret_str = ""
    for i in range(len(Text)) :
       if(Text[i].isalpha()==True) :
        ret_str+=Text[i].upper()

    return ret_str

def vignere_cipher(plain_list,key,mode):
    ####### fill the Key string ###########
    cipher_list=[]
    #print(plain_list)
    for plain_txt in plain_list :
       # print(plain_txt)
        Modified_str=srtToUpper(plain_txt)
        key_str=""
        key_str+=key
        cipher_str=""
        #print(Modified_str)
        for i in range (len(Modified_str)):
            #update the rest of the key based on the mode autp or repeating mode
            if (i >= len(key)):
                if (mode == False):
                    #repated mode
                    key_str+=key[i%len(key)]
                else :
                    #auto mode
                    key_str+=Modified_str[i]

                # add the key and update the cipher text #
            #print(key_str)
            cipher_str+=alpha[(alpha.find(Modified_str[i])+alpha.find(key_str[i]))%26]
                #cipher_str+=chr((ord(Modified_str[i])+ord(key_str[i])-65)%26+65)
        #print(cipher_str)
        cipher_list.append(cipher_str+"\n")
    print(cipher_list)
    return cipher_list

#vignere_cipher(["MAKEITHAPPEN"],"MATH")
