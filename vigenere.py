plaintext = input("Enter a word : ")
keyword = input("Enter a keyword : ")

def encrypt_vigenere(plaintext: str, keyword: str) -> str :
        
    """

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    i=0
    ciphertext = ''
    while len(keyword) <  len(plaintext) :
        if i >= len(keyword) :
            i = 0
            keyword += keyword[i]
            i += 1
        else :
            keyword += keyword[i]
            i += 1
    i = 0
    while i < len(plaintext) :
        size = plaintext[i].islower()
        if ord(plaintext[i]) < 65 or 90 < ord(plaintext[i]) < 97 or ord(plaintext[i]) > 122 : 
                    ciphertext = ciphertext + plaintext[i]
        else:
            meme = ord(keyword[i])
            if meme < 91 and meme > 64 :
                meme -= 65
            elif meme < 123 and meme > 96 :
                meme -= 97
            promejytochnoe = ord(plaintext[i])
            promejytochnoe += meme
            if promejytochnoe > 90 and size == False :
                promejytochnoe -= 26
            elif promejytochnoe > 122 and size == True :
                promejytochnoe -= 26
            word = chr(promejytochnoe)
            ciphertext = ciphertext + word
        i += 1
    return (ciphertext)

ciphertext = encrypt_vigenere(plaintext, keyword)

def decrypt_vigenere(ciphertext: str, keyword: str) -> str :
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    i=0
    plaintext = ''
    while len(keyword) <  len(ciphertext) :
        if i >= len(keyword) :
            i = 0
            keyword += keyword[i]
            i += 1
        else :
            keyword += keyword[i]
            i += 1
    i = 0
    while i < len(ciphertext) :
        size = ciphertext[i].islower()
        if ord(ciphertext[i]) < 65 or 90 < ord(ciphertext[i]) < 97 or ord(ciphertext[i]) > 122 : 
                    plaintext = plaintext + ciphertext[i]
        else:
            meme = ord(keyword[i])
            if meme < 91 and meme > 64 :
                meme -= 65
            elif meme < 123 and meme > 96 :
                meme -= 97
            promejytochnoe = ord(ciphertext[i])
            promejytochnoe -= meme
            if size == False and  promejytochnoe < 65  :
                promejytochnoe += 26
            elif size == True and promejytochnoe < 97 :
                promejytochnoe += 26
            word = chr(promejytochnoe)
            plaintext = plaintext + word
        i += 1
    return (plaintext)



print (encrypt_vigenere(plaintext, keyword))
print (decrypt_vigenere(ciphertext, keyword))


