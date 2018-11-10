
def caesar_alg(plain_string,key):
    cipher_text=[]
    cipher_string=""
    print(plain_string)
    for line in plain_string:
        str_data=""
        for i in range(len(line)) :
            #cipher_text.append("")
            #print(line)
            if(line[i].isupper()):
                #line.replace((line[i]),chr((ord(line[i])+key-65)%26+65))
                str_data += chr((ord(line[i])+key-65)%26+65)
            elif(line[i].islower()):
                #line.replace((line[i]), chr(ord(line[i]) + key))
                str_data+= chr((ord(line[i])+key-97)%26 +97) #97 is the asci of a
                #print(line)
        cipher_text.append(str_data+'\n')
    return cipher_text