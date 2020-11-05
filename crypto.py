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
    completely_arbitrary_max = 10
    W = [rand.randint(0, completely_arbitrary_max)]
    for i in range(1, n):
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
        bit_list = [int(z) for z in bin(ord(i))[2:].zfill(8)] 
        #makes the list of bits of the ASCII value of the character i in plaintext
        A.append(sum([bit_list[i] * public_key[i] for i in range(len(bit_list))])) 
        #appends the sum of the bit * the random integer in B to the end of the list A
    return A

def find_S(R, Q):
    for S in range(2, Q) : 
        if ((R * S) % Q == 1) : 
            return S 
    return

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    W = list(private_key[0])
    W.reverse() #reverse the superincreasing series to use it for creating the binary representation of the character
    Q = private_key[1]
    R = private_key[2]
    S = find_S(R, Q)
    to_ret = []
    for C in ciphertext:
        bit_list = []
        C_prime = (C * S) % Q 
        # bit_list = [0 if j > C else 1 C:= C-j for j in W] 
        # ^This is the list comprehension version of the for loop below but I don't know the := operator well enough to make it work
        for j in W:
            # print(i)
            if j <= C_prime:
                bit_list.append(1)
                C_prime = C_prime - j
            else:
                 bit_list.append(0)

        bit_list.reverse()
        del bit_list[8:] #truncate the binary to 8 bits just in case the user gave a private key with W > 8 since n was hardcoded to 8 at the start
        bit_list = "".join([str(x) for x in bit_list])
        to_ret.append(chr(int(bit_list, 2)))
        #convert the string of bits from binary to decimal then convert that to a char and append it to the return string
    return "".join(to_ret)


def main():
    # Testing code here
    #cesar
    # offset = 25
    # enc = encrypt_caesar("AB", offset)
    # print(enc)
    # print(decrypt_caesar(enc, offset))

    #vignere
    # key = "XYZZYZ"
    # enc = encrypt_vigenere("SHORTERKEY", key)
    # print(enc)
    # print(decrypt_vigenere(enc, key))

    #mhkc
    private_key = ((6, 12, 20, 51, 137, 231, 845, 1319, 4823), 13976, 3)
    public_key_answer = (18, 36, 60, 153, 411, 693, 2535, 3957, 493)
    public_key = create_public_key(private_key)
    # print("My public key: " + str(public_key)) 
    print("Public Key is the right answer: " + str(public_key == public_key_answer))
    to_encrypt = "MICHAELTHIBODEAUX"
    enc = encrypt_mhkc(to_encrypt, public_key)
    encryption_answer = [5097, 4404, 6528, 447, 3993, 4686, 1140, 882, 447, 4404, 2571, 7632, 729, 4686, 3993, 4839, 600]
    print("Encryption is the right answer: " + str(enc == encryption_answer))

    dec = decrypt_mhkc(encryption_answer, private_key)
    print("My decryption: " + str(dec) + " is the right answer: " + str(dec == to_encrypt))

if __name__ == "__main__":
    main()