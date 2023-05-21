message = "ACT"
key = "GYBNQKURP"

keyMatrix = [[0]*3 for i in range(3)]
print(keyMatrix)

messageMatrix = [[0] for i in range(3)]
print(messageMatrix)

cypherMatrix = [[0] for i in range(3)]
print(cypherMatrix)


k = 0
for i in range(3):
    for j in range(3):
        keyMatrix[i][j] = ord(key[k]) - 65
        k += 1

print(keyMatrix)


for i in range(3):
    messageMatrix[i][0] = ord(message[i])-65
print(messageMatrix)

cypherText = []
for i in range(3):
    for j in range(1):
        cypherMatrix[i][j] = 0
        for x in range(3):
            cypherMatrix[i][j] += (keyMatrix[i][x] * messageMatrix[x][j])
        cypherMatrix[i][j] = chr(cypherMatrix[i][j] % 26 + 65)
    cypherText.append(cypherMatrix[i][0])

print(cypherMatrix)
print(cypherText)

cipher = "".join(cypherText)

print(cipher)
