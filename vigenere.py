plaintext = input("Enter a word : ")
keyword = input("Enter a keyword : ")


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    i = 0
    ciphertext = ''
    while len(keyword) < len(plaintext):
        if i >= len(keyword):
            i = 0
            keyword += keyword[i]
            i += 1
        else:
            keyword += keyword[i]
            i += 1
    i = 0
    while i < len(plaintext):
        if ord('A') > ord(plaintext[i]) or ord('Z') < ord(plaintext[i]) < ord('a') or ord(plaintext[i]) > ord('z'):
            ciphertext += plaintext[i]
        else:
            s = ord(keyword[i])
            if s < (ord('Z') + 1) and s > (ord('A') - 1):
                s -= ord('A')
            elif s < (ord('z') + 1) and s > (ord('a') - 1):
                s -= ord('a')
            s += ord(plaintext[i])
            if 'a' <= plaintext[i] <= 'z' and s > ord('z'):
                s -= 26
            elif 'A' <= plaintext[i] <= 'Z' and s > ord('Z'):
                s -= 26
            ciphertext += chr(s)
        i += 1
    return (ciphertext)


ciphertext = encrypt_vigenere(plaintext, keyword)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    i = 0
    plaintext = ''
    while len(keyword) < len(ciphertext):
        if i >= len(keyword):
            i = 0
            keyword += keyword[i]
            i += 1
        else:
            keyword += keyword[i]
            i += 1
    i = 0
    while i < len(ciphertext):
        if ord('A') > ord(ciphertext[i]) or ord('Z') < ord(ciphertext[i]) < ord('a') or ord(ciphertext[i]) > ord('z'):
            plaintext += ciphertext[i]
        else:
            size = ciphertext[i].islower()
            s = ord(keyword[i])
            if s < (ord('Z') + 1) and s > (ord('A') - 1):
                s -= ord('A')
            elif s < (ord('z') + 1) and s > (ord('a') - 1):
                s -= ord('a')
            s = ord(ciphertext[i]) - s
            if size == False and s < ord('A'):
                s += 26
            elif size == True and s < ord('a'):
                s += 26
            plaintext += chr(s)
        i += 1
    return (plaintext)


print(encrypt_vigenere(plaintext, keyword))
print(decrypt_vigenere(ciphertext, keyword))
