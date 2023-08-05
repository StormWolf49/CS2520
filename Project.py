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

#Vignere Encrypt
def vignereE(text, key):
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
     
#Vignere Decrypt
def vignereD(cipher_text, key):
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
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

#Matrix Inverse Modulo
def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modulus_inv

#Hill Encrypt
def hillE(text, K):
    encrypted = ""
    message_in_numbers = []
    for letter in text:
        message_in_numbers.append(letter_to_index[letter])
    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]
    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]
        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]
    return encrypted

#Hill Decrypt
def hillD(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []
    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])
    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]
    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]
        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]
    return decrypted


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
        print("What do you want to do next:\n  (0) Exit\n  (1) Caesar\n  (2) Vignere\n  (3) Hill\n  (4) Affline\n  (5) Atbash")
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
                key = int(input("Enter encryption key: "))
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
                #Vignere
                print("Vignere Cipher:")
                text = input("Text to be encrypted/decrypted: ")
                key = input("Enter encryption key: ")
                c = int(input("(1)Encrypt or (2)Decrypt: "))
                print (f"Text: {text}")
                print (f"Key: {key}")
                match c:
                    case 1:
                        print (f"Cipher: {vignereE(text,key)}")
                    case 2:
                        print (f"De-Ciphered: {vignereD(text, key)}")
                print("")
            case 3:
                #Hill
                print("Hill Cipher:")
                text = input("Text to be encrypted/decrypted: ")
                K = np.matrix([[3, 3], [2, 5]])
                Kinv = matrix_mod_inv(K, len(alphabet))
                c = int(input("(1)Encrypt or (2)Decrypt: "))
                print(f"Text: {text}")
                match c:
                    case 1:
                        print (f"Cipher: {hillE(text, K)}")
                    case 2:
                        print (f"De-Ciphered: {hillD(text, Kinv)}")
                print("")
            case 4:
                #Affline
                print("Affline Cipher:")
                text = input("Text to be encrypted/decrypted: ")
                k1 = int(input("Enter encryption key1: "))
                k2 = int(input("Enter encryption key2: "))
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

    #Vignere
    print("Vignere Cipher:")
    text = "AMAZING"
    print (f"Text: {text}")
    key = "SUP"
    print (f"Key: {key}")
    cipher_text = vignereE(text,key)
    print(f"Cipher: {cipher_text}")
    print(f"De-Ciphered: {vignereD(cipher_text, key)}")
    print("")

    #Hill
    print("Hill Cipher:")
    text = "help"
    K = np.matrix([[3, 3], [2, 5]])
    Kinv = matrix_mod_inv(K, len(alphabet))
    print(f"Text: {text}")
    print(f"Cipher: {hillE(text, K)}")
    print(f"De-Ciphered: {hillD(hillE(text, K), Kinv)}")
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