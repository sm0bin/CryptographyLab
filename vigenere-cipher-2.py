# massage = input("Enter Massage: ").lower()
# key = input("Input Key: ").lower()

massage = "Geeks for Geeks!"
key = "Ayush"
massage = massage.lower()
key = key.lower()


def encrypt(massage, key):
    cipherText = ""
    keyIndex = 0
    for ch in massage:
        if ch.isalpha():
            shift = ord(key[keyIndex]) - ord('a')
            mIndex = ord(ch)-ord('a') + shift
            shiftChar = chr(mIndex % 26 + ord('a'))
            cipherText += shiftChar
            keyIndex = (keyIndex + 1) % len(key)
        else:
            cipherText += ch

    return cipherText


def decrypt(cipher, key):
    plainText = ""
    keyIndex = 0
    for ch in cipher:
        if ch.isalpha():
            shift = ord(key[keyIndex]) - ord('a')
            mIndex = ord(ch)-ord('a') - shift
            shiftChar = chr(mIndex % 26 + ord('a'))
            plainText += shiftChar
            keyIndex = (keyIndex + 1) % len(key)
        else:
            plainText += ch

    return plainText


cipherText = encrypt(massage, key)
plainText = decrypt(cipherText, key)


print(cipherText)
print(plainText)
