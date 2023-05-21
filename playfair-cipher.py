dic = {}
str = "abcdefghiklmnopqrstuvwxyz"


def addFiller(plainText):
    i = 0
    while i < len(plainText)-1:
        if plainText[i] == plainText[i+1]:
            plainText = plainText[:i+1] + 'x' + plainText[i+1:]
        i += 2
    if len(plainText) % 2 != 0:
        plainText += 'z'

    return plainText


def keyGeneration(key):
    usedLetters = []
    key = key.replace('j', 'i')
    matrix = [['' for i in range(5)] for j in range(5)]
    row, col = 0, 0
    for letter in key:
        if letter not in usedLetters:
            matrix[row][col] = letter
            dic[letter] = (row, col)
            usedLetters.append(letter)
            col += 1
        if col > 4:
            col = 0
            row += 1
    for letter in str:
        if letter not in usedLetters:
            matrix[row][col] = letter
            dic[letter] = (row, col)
            usedLetters.append(letter)
            col += 1
        if col > 4:
            col = 0
            row += 1
    return matrix


key = input("Enter a key: ").lower()
plainText = input("Enter a plaintext: ").lower()


print(keyGeneration(key))
print(addFiller(plainText))


def encrypt(plainText, key):
    keyMatrix = keyGeneration(key)
    plainText = addFiller(plainText)
    cypherText = ""

    for i in range(0, len(plainText), 2):
        row1, col1 = dic[plainText[i]]
        row2, col2 = dic[plainText[i+1]]
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        col1, col2 = col2, col1
        cypherText += keyMatrix[row1][col1] + keyMatrix[row2][col2]
    return cypherText


cypherText = encrypt(plainText, key)
print(cypherText)


def decrypt(plainText, key):
    keyMatrix = keyGeneration(key)
    plainText = addFiller(plainText)
    cypherText = ""

    for i in range(0, len(plainText), 2):
        row1, col1 = dic[plainText[i]]
        row2, col2 = dic[plainText[i+1]]
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        col1, col2 = col2, col1
        cypherText += keyMatrix[row1][col1] + keyMatrix[row2][col2]
    return cypherText


plainText = decrypt(cypherText, key)
print(plainText)
