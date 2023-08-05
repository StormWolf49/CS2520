#Name: Nikhil Kowdle
#Final Project
#Simply run the file to access the various different cipher's encyption/decryption tools.


import numpy as np
from egcd import egcd

#Caesar Cipher Encrypt
def caesarE(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

#Caesar Cipher Decrypt
def caesarD(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


#Vigenere Cipher
def generateKey(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

#Vigenere Encrypt
def vigenereE(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text) -
                       len(key)):
            key.append(key[i % len(key)])
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) +
             ord(key[i])) % 26
        x += ord("A")
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
#Vigenere Decrypt
def vigenereD(cipher_text, key):
    key = list(key)
    if len(cipher_text) == len(key):
        return(key)
    else:
        for i in range(len(cipher_text) -
                       len(key)):
            key.append(key[i % len(key)])
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord("A")
        orig_text.append(chr(x))
    return("" . join(orig_text))


#Hill Cypher
def create_matrix_from(key):
    m=[[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m

def MatrixInverse(K):
    det = int(np.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = np.delete(Dji, (j), axis=0)
            Dji = np.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv

def encrypt(P, K):
    C=[0,0,0]
    C[0] = (K[0][0]*P[0] + K[1][0]*P[1] + K[2][0]*P[2]) % 26
    C[1] = (K[0][1]*P[0] + K[1][1]*P[1] + K[2][1]*P[2]) % 26
    C[2] = (K[0][2]*P[0] + K[1][2]*P[1] + K[2][2]*P[2]) % 26
    return C

#Hill Encrypt/Decrypt
def hill(message, K):
    cipher_text = []
    #Transform the message 3 characters at a time
    for i in range(0,len(message), 3):
        P=[0, 0, 0]
        #Assign the corresponfing integer value to each letter
        for j in range(3):
            P[j] = ord(message[i+j]) % 65
        #Encript three letters
        C = encrypt(P,K)
        #Add the encripted 3 letters to the final cipher text
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
        #Repeat until all sets of three letters are processed.
        
    #return a string
    return "".join(cipher_text)


#Affine Cipher
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
 
#Affine Encrypt
def affineE(text, key):
    return "".join([ chr((( key[0]*(ord(t) - ord("A")) + key[1] ) % 26)
                  + ord("A")) for t in text.upper().replace(" ", "") ])
 
#Affine Decrypt
def affineD(cipher, key):
    return "".join([ chr((( modinv(key[0], 26)*(ord(c) - ord("A") - key[1]))
                    % 26) + ord("A")) for c in cipher ])


#Atbash Cipher
lookup_table = {"A" : "Z", "B" : "Y", "C" : "X", "D" : "W", "E" : "V",
        "F" : "U", "G" : "T", "H" : "S", "I" : "R", "J" : "Q",
        "K" : "P", "L" : "O", "M" : "N", "N" : "M", "O" : "L",
        "P" : "K", "Q" : "J", "R" : "I", "S" : "H", "T" : "G",
        "U" : "F", "V" : "E", "W" : "D", "X" : "C", "Y" : "B", "Z" : "A"}

#Atbash Encrypt/Decrypt
def atbash(text):
    cipher = ""
    for letter in text:
        if(letter != " "):
            cipher += lookup_table[letter]
        else:
            cipher += " "
    return cipher


#User Input
def user():
    print("DEMO COMPLETE")
    while True:
        print("What do you want to do next:\n  (0) Exit\n  (1) Caesar\n  (2) Vigenere\n  (3) Hill\n  (4) Affline\n  (5) Atbash")
        choice = int(input(""))
        print("")
        match choice:
            case 0:
                print("Exiting, goodbye")
                break
            case 1:
                #Caesar
                print("Caesar Cipher:")
                text = input("Text to be encrypted/decrypted: ")
                key = int(input("Enter encryption key (Integer): "))
                c = int(input("(1)Encrypt or (2)Decrypt: "))
                print (f"Text: {text}")
                print (f"Shift: {str(key)}")
                match c:
                    case 1:
                        print (f"Cipher: {caesarE(text,key)}")
                    case 2:
                        print (f"De-Ciphered: {caesarD(text,key)}")
                print("")
            case 2:
                #Vigenere
                print("Vigenere Cipher:")
                text = input("Text to be encrypted/decrypted: ")
                key = input("Enter encryption key (Integer): ")
                c = int(input("(1)Encrypt or (2)Decrypt: "))
                print (f"Text: {text}")
                print (f"Key: {key}")
                match c:
                    case 1:
                        print (f"Cipher: {vigenereE(text,key)}")
                    case 2:
                        print (f"De-Ciphered: {vigenereD(text, key)}")
                print("")
            case 3:
                #Hill
                print("Hill Cipher:")
                text = input("Text to be encrypted/decrypted (Length of a multiple of 3, including spaces): ")
                key = input("Enter encryption key (All caps, length of a multiple of 3, at least 9 long, including spaces): ")
                K = create_matrix_from(key)
                Kinv = MatrixInverse(K)
                c = int(input("(1)Encrypt or (2)Decrypt: "))
                print(f"Text: {text}")
                print (f"Key: {key}")
                match c:
                    case 1:
                        print (f"Cipher: {hill(text, K)}")
                    case 2:
                        print (f"De-Ciphered: {hill(text, Kinv)}")
                print("")
            case 4:
                #Affline
                print("Affline Cipher:")
                text = input("Text to be encrypted/decrypted: ")
                k1 = int(input("Enter encryption key1 (Integer): "))
                k2 = int(input("Enter encryption key2 (Integer): "))
                key = [k1, k2]
                c = int(input("(1)Encrypt or (2)Decrypt: "))
                print(f"Text: {text}")
                print (f"Key: {key}")
                match c:
                    case 1:
                        print (f"Cipher: {affineE(text, key)}")
                    case 2:
                        print (f"De-Ciphered: {affineD(text, key)}")
                print("")
            case 5:
                #Atbash
                print("Atbash Cipher:")
                text = input("Text to be encrypted/decrypted: ")
                c = int(input("(1)Encrypt or (2)Decrypt: "))
                print(f"Text: {text}")
                match c:
                    case 1:
                        print (f"Cipher: {atbash(text.upper())}")
                    case 2:
                        print (f"De-Ciphered: {atbash(text.upper())}")
                print("")
    

#Main Function
def main():
    #Caesar
    print("Caesar Cipher:")
    text = "ATTACKATONCE"
    s = 4
    print (f"Text: {text}")
    print (f"Shift: {str(s)}")
    print (f"Cipher: {caesarE(text,s)}")
    print (f"De-Ciphered: {caesarD(caesarE(text,s),s)}")
    print("")

    #Vigenere
    print("Vigenere Cipher:")
    text = "AMAZING"
    print (f"Text: {text}")
    key = "SUP"
    print (f"Key: {key}")
    cipher_text = vigenereE(text,key)
    print(f"Cipher: {cipher_text}")
    print(f"De-Ciphered: {vigenereD(cipher_text, key)}")
    print("")

    #Hill
    print("Hill Cipher:")
    text = "MYSECRETMESSAGE"
    print(f"Text: {text}")
    key = "RRFVSVCCT"
    print (f"Key: {key}")
    K = create_matrix_from(key)
    Kinv = MatrixInverse(K) 
    print(f"Cipher: {hill(text, K)}")
    print(f"De-Ciphered: {hill(hill(text, K), Kinv)}")
    print("")

    #Affline
    print("Affline Cipher:")
    text = "AFFLINE CIPHER"
    print(f"Text: {text}")
    key = [17, 20]
    print (f"Key: {key}")
    affine_encrypted_text = affineE(text, key)
    print(f"Cipher: {affine_encrypted_text}")
    print(f"De-Ciphered: {affineD(affine_encrypted_text, key)}")
    print("")

    #Atbash
    print("Atbash Cipher:")
    text = "THIS IS A CIPHER"
    print(f"Text: {text}")
    print(f"Cipher: {atbash(text.upper())}")
    print(f"De-Ciphered: {atbash(atbash(text.upper()))}")
    print("")

    user()
 
 
main()