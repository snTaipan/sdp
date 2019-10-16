def encrypt_caesar(plaintext: str) -> str :
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    i = 0
    ciphertext = ""
    while i < len(plaintext) :
        if 'a' <= plaintext[i] <= 'z' or 'A' <= plaintext[i] <= 'Z':
            s = ord(plaintext[i]) + 3
            if s > ord('Z') and s < ord('a') or s > ord('z') :
                s = s - 26
            ciphertext = ciphertext + chr(s)
        else:
            ciphertext = ciphertext + plaintext[i]
        i = i+1
    return(ciphertext)

def decrypt_caesar(ciphertext: str) -> str :
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    i = 0
    plaintext = ""
    while i < len(ciphertext) :
        if 'a' <= ciphertext[i] <= 'z' or 'A' <= ciphertext[i] <= 'Z' :
            s = ord(ciphertext[i]) - 3
            if s < ord('a') and s > ord('Z') or s < ord('A'):
                s = s + 26
            plaintext = plaintext + chr(s)
        else :
            plaintext = plaintext + ciphertext[i]
        i = i+1
    return(plaintext)

plaintext = input("Enter a word: ")
ciphertext = encrypt_caesar(plaintext)
print (ciphertext)
plaintext = decrypt_caesar(ciphertext)
print (plaintext)
