def encrypt_caesar(plaintext):
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
    ciphertext = ''
    for char in plaintext:
        if 'A' <= char <= 'z':
            new_word = chr(ord(char)+3)
            if char == 'x':
                new_word = 'a'
            elif char == 'y':
                new_word = 'b'
            elif char == 'z':
                new_word = 'c'
            elif char == 'X':
                new_word ='A'
            elif char == 'Y':
                new_word = 'B'
            elif char == 'Z':
                new_word = 'A'
            ciphertext = ciphertext + new_word
        else:
            ciphertext = ciphertext + char
    return ciphertext
print(encrypt_caesar("Python3.6"))
def decrypt_caesar(ciphertext):
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
    plaintext = ''
    for char in ciphertext:
        if 'A' <= char <= 'z':
            new_word = chr(ord(char) - 3)
            if char == 'a':
                new_word = 'x'
            elif char == 'b':
                new_word = 'y'
            elif char == 'c':
                new_word = 'z'
            elif char == 'A':
                new_word = 'X'
            elif char == 'B':
                new_word = 'Y'
            elif char == 'A':
                new_word = 'Z'
            plaintext = plaintext + new_word
        else:
            plaintext = plaintext + char
    return plaintext
print(decrypt_caesar("sbwkrq"))

