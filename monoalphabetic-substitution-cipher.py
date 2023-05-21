import random


def generateKey():
    characters = list('abcdefghijklmnopqrstuvwx')
    random.shuffle(characters)
    key = ''.join(characters)
    return key


def encrypt(plainText, key):
    cipherText = ""
    # plainText = plainText.lower()
    for ch in plainText:
        if ch.isalpha():
            index = ord(ch)-ord('a')
            cipherChar = key[index]
            cipherText += cipherChar
        else:
            cipherText += ch

    return cipherText


def decrypt(cipherText, key):
    plainText = ""
    for ch in cipherText:
        if ch.isalpha():
            index = key.index(ch)
            decipherChar = chr(index + ord('a'))
            plainText += decipherChar
        else:
            plainText += ch
    return plainText


text = input("Enter Text: ").lower()
key = generateKey()
cipherText = encrypt(text, key)
decipherText = decrypt(cipherText, key)

print("Key: ", key)
print("Cipher Text: ", cipherText)
print("Decipher Text: ", decipherText)
