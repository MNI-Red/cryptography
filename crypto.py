A = ord("A")
Z = ord("Z")

def offset_char(char, offset):
    return chr(((ord(char) + offset) - A)%(Z - A + 1) +A) #The inner arithmetic always returns an ASCII value from A to Z

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
    key_string = (len_in//len_key)*keyword + keyword[,len_in%len_key]
    print(key_string)
    for i in range(len_in):
        offset_char(plaintext[i], ord(plaintext[i])-ord(key_string[i]))

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    #this method is exactly the same as the previous one but the offset is negative
    len_in = len(ciphertext)
    len_key = len(keyword)
    key_string = (len_in//len_key)*keyword + keyword[,len_in%len_key]
    print(key_string)
    for i in range(len_in):
        offset_char(plaintext[i], ord(key_string[i]) - ord(plaintext[i]))

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    enc = encrypt_vigenere("ATTACKATDAWN", "LEMON")
    print(enc)
    print(decrypt_caesar(enc, "LEMON"))

if __name__ == "__main__":
    main()