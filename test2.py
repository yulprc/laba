def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    if len(keyword) > len(plaintext):
        keyword = keyword[:len(plaintext)]
    while len(keyword) < len(plaintext):
        keyword = keyword + keyword
        keyword = keyword[:len(plaintext)]
    for index in range(len(plaintext)):
        plaintext_index = plaintext[index]
        cipher_index = keyword[index]
        cipher_index = cipher_index.lower()
        bias = ord(cipher_index) - ord('a')
        new_index = ord(plaintext_index) + bias
        if plaintext_index.isupper() and new_index > ord('Z'):
            new_index = new_index - ord('[') + ord('A')
        elif plaintext_index.islower() and new_index > ord('z'):
            new_index = new_index -  ord('{') + ord('a')
        ciphertext = ciphertext + chr(new_index)
    return ciphertext

print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))

def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    if len(keyword) > len(ciphertext):
        keyword = keyword[:len(ciphertext)]
    while len(keyword) < len(ciphertext):
        keyword = keyword + keyword
        keyword = keyword[:len(ciphertext)]
    for index in range(len(ciphertext)):
        cipertext_index = ciphertext[index]
        plain_index = keyword[index]
        plain_index = plain_index.lower()
        bias = ord(plain_index) - ord('a')
        new_index = ord(cipertext_index) - bias
        if cipertext_index.isupper() and new_index < ord('A'):
            new_index = new_index - ord('@') + ord('Z')
        elif cipertext_index.islower() and new_index < ord('a'):
            new_index = new_index - ord("'") + ord('z')
        plaintext = plaintext + chr(new_index)
    return plaintext

print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
