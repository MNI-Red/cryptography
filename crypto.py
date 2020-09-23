import random as rand
import math

A = ord("A")
Z = ord("Z")

def offset_char(char, offset):
    # print(char, offset)
    to_ret = chr(((ord(char) + offset) - A)%(Z - A + 1) +A) #The inner arithmetic always returns an ASCII value from A to Z
    # print(to_ret)
    return to_ret

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    to_ret = ""
    if plaintext: #make sure it's not empty
        for i in plaintext:
            if A <= ord(i) <= Z:
                to_ret += offset_char(i, offset)
            else:
                to_ret += i 
        return to_ret
    return plaintext

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    return encrypt_caesar(ciphertext, -offset) 
    #this function is really nothing more than the encryption but with a negative cypher

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    len_in = len(plaintext)
    len_key = len(keyword)
    key_string = (len_in//len_key)*keyword + keyword[:(len_in%len_key)]
    # print(key_string)
    to_ret = ""
    for i in range(len_in):
        to_ret += offset_char(plaintext[i], ord(key_string[i])%A)
    return to_ret

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    #this method is exactly the same as the previous one but the offset is negative
    len_in = len(ciphertext)
    len_key = len(keyword)
    key_string = (len_in//len_key)*keyword + keyword[:(len_in%len_key)]
    # print(key_string)
    to_ret = ""
    for i in range(len_in):
        to_ret += offset_char(ciphertext[i], -(ord(key_string[i])%A))
    return to_ret

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    W = []
    for i in range(n+1):
        W.append(rand.randint(sum(W)+1, sum(W)*2))
    Q = W.pop(-1)
    W = tuple(W)
    R = coprime(Q) 
    return (W, Q, R)

def coprime(a):
    co = a
    while gcd(a, co) != 1:
        co = rand.randint(2, a-1)
    return co

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    B = []
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    for i in W:
        B.append(R*i%Q)
    return tuple(B)

# Arguments: string, tuple (B)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    A = []
    for i in plaintext:
        bit_list = [int(z) for z in bin(ord(i)).zfill(8)]  
        #makes the list of bits of the ASCII value of the character i in plaintext
        A.append(sum([bit_list[i] * public_key[i] for i in range(len(bit_list))])) 
        #appends the sum of the bit * the random integer in B to the end of the list A
    return A

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    to_ret = ""
    for i in ciphertext:
        bit_list = []
        # bit_list = [0 if j > 1 else 1 and i:= i-j for j in W.reverse()]
        for j in W.reverse():
            if j > i:
                bit_list.append(0)
            else:
                bit_list.append(1)
                i = i - j
        to_ret.append(chr(int(''.join(bit_list), 2))) 
        #convert the string of bits from binary to decimal then convert that to a char and append it to the return string
    return to_ret


def main():
    # Testing code here
    enc = encrypt_vigenere("ATTACKATDAWN", "LEMON")
    print(enc)
    print(decrypt_vigenere(enc, "LEMON"))

if __name__ == "__main__":
    main()