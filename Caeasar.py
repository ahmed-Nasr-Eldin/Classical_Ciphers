
def caesar_alg(plain_list,key):
    cipher_text=[]
    cipher_string=""
    for line in plain_list:
        str_data=""
        for i in range(len(line)) :
            if(line[i].isupper()):
                str_data += chr((ord(line[i])+key-65)%26+65)
            elif(line[i].islower()):
                str_data+= chr((ord(line[i])+key-97)%26 +97) #97 is the asci of a
        cipher_text.append(str_data+'\n')
    return cipher_text