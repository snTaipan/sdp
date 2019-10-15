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
        if ord(plaintext[i]) < 65 or 90 < ord(plaintext[i]) < 97 or ord(plaintext[i]) > 122 : 
                ciphertext = ciphertext + plaintext[i]
        else :  
            if plaintext[i] == 'X':
                word = 'A'
            elif plaintext[i] == 'Y':
                word = 'B' 
            elif plaintext[i] == 'Z':
                word = 'C' 
            elif plaintext[i] == 'x':
                word = 'a'
            elif plaintext[i] == 'y':
                word = 'b' 
            elif plaintext[i] == 'z':
                word = 'c' 
            else:
                s = ord(plaintext[i])
                s = s+3
                word = chr(s)
            ciphertext = ciphertext + word
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
        if ord(ciphertext[i]) < 65 or 90 < ord(ciphertext[i]) < 97 or ord(ciphertext[i]) > 122 : 
                plaintext = plaintext + ciphertext[i]
        else :   
            if ciphertext[i] == 'A':
                word = 'X'
            elif ciphertext[i] == 'B':
                word = 'Y' 
            elif ciphertext[i] == 'C':
                word = 'Z' 
            elif ciphertext[i] == 'a':
                word = 'x'
            elif ciphertext[i] == 'b':
                word = 'y' 
            elif ciphertext[i] == 'c':
                word = 'z' 
            else:
                s = ord(ciphertext[i])
                s = s-3
                word = chr(s)
            plaintext = plaintext + word
        i = i+1
    return(plaintext)

plaintext = input("Enter a word: ")
ciphertext = encrypt_caesar(plaintext)
print (ciphertext)
plaintext = decrypt_caesar(ciphertext)
print (plaintext)
