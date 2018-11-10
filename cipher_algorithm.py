import os
#from PlayFair import play_fair
#from Caesar import caesar_alg
import Caeasar as Cs
import PlayFair as Pf
import Hill as Hi
import Vigenere as Vi
import Vernam as Vr
print('plz Enter your prefered algorithm ')
selectedAlgorithm = input()
cipher_path = "./"
plain_file= None
cipher_file=None
plain_path='./'
cipher_text = []
if(selectedAlgorithm.lower() == '1' ):
#if(selectedAlgorithm.lower() == 'caesar' ):
    cipher_path += "Caesar/caesar_cipher.txt"
    plain_path += "Caesar/caesar_plain.txt"
    plain_file=open(plain_path,"r")
    cipher_text=Cs.caesar_alg(plain_file.readlines(),2)      #function takes two arguments text and key
    print(cipher_text)
elif((selectedAlgorithm.lower() == '2' )):
    cipher_path += "PlayFair/playfair_cipher.txt"
    plain_path += "PlayFair/playfair_plain.txt"
    plain_file = open(plain_path, "r")
    cipher_text=Pf.play_fair(plain_file.readlines(),'PLAYFAIREXAMPLE')
elif((selectedAlgorithm.lower() == '3' )):
    cipher_path += "Hill/hill_cipher_2x2.txt"
    plain_path += "Hill/hill_plain_2x2.txt"
    matrix_key=[[5,17],[8,3]]
    plain_file = open(plain_path, "r")
    cipher_text=Hi.hill_cipher_2x2(plain_file.readlines(),matrix_key)
elif((selectedAlgorithm.lower() == '4' )):
    cipher_path += "Hill/hill_cipher_3x3.txt"
    plain_path += "Hill/hill_plain_3x3.txt"
    matrix_key=[[2,14,12],[9,1,6],[7,5,3]]
    plain_file = open(plain_path, "r")
    cipher_text=Hi.hill_cipher_3x3(plain_file.readlines(),matrix_key)
elif ((selectedAlgorithm.lower() == '5')):
    cipher_path += "Vigenere/vigenere_cipher.txt"
    plain_path += "Vigenere/vigenere_plain.txt"
    key = "PIE"
    plain_file = open(plain_path, "r")
    cipher_text = Vi.vignere_cipher(plain_file.readlines(),key,False)
elif ((selectedAlgorithm.lower() == '6')):
    cipher_path += "Vernam/vernam_cipher.txt"
    plain_path += "Vernam/vernam_plain.txt"
    key = "SPARTAN"
    plain_file = open(plain_path, "r")
    cipher_text = Vr.vernam_cipher(plain_file.readlines(),key)
    print(cipher_text)
########################## write the ouput cipher Text ########################################333

if(cipher_path != './') :  #one of algorithms has been selected
    cipher_file=open(cipher_path,"w")
    #for ciph_msg in cipher_text :
    cipher_file.writelines(cipher_text)
    cipher_file.close()
    plain_file.close()








