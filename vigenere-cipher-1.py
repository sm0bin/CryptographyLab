m = "Geeks. for Geeks!"
key = "AYUSH"


def encryption(plainText, key):
    cypherText = ""
    keyIndex = 0
    for ch in plainText:
        if ch.isalpha():
            shift = ord(key[keyIndex].upper())-65
            shiftChar = chr((ord(ch.upper())-65+shift) % 26 + 65)
            if ch.isupper():
                cypherText += shiftChar
            else:
                cypherText += shiftChar.lower()
            keyIndex = (keyIndex+1) % len(key)
        else:
            cypherText += ch

    return cypherText


def decryption(cypherText, key):
    plainText = ""
    keyIndex = 0
    for ch in cypherText:
        if ch.isalpha():
            shift = ord(key[keyIndex].upper())-65
            shiftChar = chr((ord(ch.upper())-65-shift) % 26 + 65)
            if ch.isupper():
                plainText += shiftChar
            else:
                plainText += shiftChar.lower()
            keyIndex = (keyIndex+1) % len(key)
        else:
            plainText += ch

    return plainText


plainText = input("Enter Massage: ")
key = input("Enter key: ")

cypherText = encryption(plainText, key)
print(cypherText)
plainText = decryption(cypherText, key)
print(plainText)
