key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]

keyAfterP10 = [key[x-1] for x in p10]
print("key after p10: ", keyAfterP10)

leftHalf = [keyAfterP10[x] for x in range(5)]
rightHalf = [keyAfterP10[x] for x in range(5, 10)]

print("Left Half:", leftHalf)
print("Right Half:", rightHalf)

leftLS1 = []
rightLS1 = []

for i in range(1, 5):
    leftLS1.append(leftHalf[i])
leftLS1.append(leftHalf[0])

for i in range(1, 5):
    rightLS1.append(rightHalf[i])
rightLS1.append(rightHalf[0])

print("Left half after LS1: ", leftLS1)
print("Right half after LS1: ", rightLS1)

afterLS1 = leftLS1 + rightLS1
print("After LS1: ", afterLS1)


k1 = [afterLS1[x-1] for x in p8]

print("K1: ", k1)

leftLS2 = []
rightLS2 = []

for i in range(2, 5):
    leftLS2.append(leftLS1[i])
leftLS2.append(leftLS1[0])
leftLS2.append(leftLS1[1])

for i in range(2, 5):
    rightLS2.append(rightLS1[i])
rightLS2.append(rightLS1[0])
rightLS2.append(rightLS1[1])

print("Left half after LS2: ", leftLS2)
print("Right half after LS2: ", rightLS2)

afterLS2 = leftLS2 + rightLS2
print("After LS2: ", afterLS2)

k2 = [afterLS2[x-1] for x in p8]

print("K2: ", k2)
