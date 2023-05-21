p = int(input("Enter P: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

listRHS = [(x**3 + x * a + b) % p for x in range(p)]
listLHS = [(y**2) % p for y in range(p)]


def getAffinePoints():
    points = []

    for i in range(p):
        for j in range(p):
            if listRHS[i] == listLHS[j]:
                points.append((i, j))

    return points


def mulInv(num, mod):
    for i in range(mod):
        if (num*i) % mod == 1:
            return i

    return -1


print(listRHS)
print(listLHS)
print(getAffinePoints())

gPoint = input("Enter Genertor Point: ").replace(' ', '').split(",")
gPoint = (int(gPoint[0]), int(gPoint[1]))

resultPoint = gPoint


def getSubGroups(g1, g2):
    if g1[0] == g2[0] and g1[1] == g2[1]:
        s = ((3 * g1[0]**2 + a)*mulInv(2*g1[1], p)) % p
    else:
        s = ((g2[1] - g1[1])*mulInv(g2[0] - g1[0], p)) % p

    x3 = (s**2 - g1[0] - g2[0]) % p
    y3 = (s*(g1[0] - x3)-g1[1]) % p

    return (x3, y3)


print(f"Subgroup points of {gPoint}: \nG: {resultPoint}")
gNum = 2

while True:
    resultPoint = getSubGroups(resultPoint, gPoint)
    print(f"{gNum}G: {resultPoint}")
    gNum += 1

    if resultPoint[0] == gPoint[0]:
        print(f"{gNum}: 0")
        break

print(f"Number of subgroup points of {gPoint}: ", gNum)
