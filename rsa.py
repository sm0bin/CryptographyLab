p = 53  # int(input("Enter p: "))
q = 59  # int(input("Enter q: "))
e = 3  # int(input("Enter e: "))
M = 89  # int(input("Enter M: "))


def gcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a

# def gcd(a, h):
#     temp = 0
#     while (1):
#         temp = a % h
#         if (temp == 0):
#             return h
#         a = h
#         h = temp


n = p*q

phi = (p-1)*(q-1)

while True:
    if gcd(phi, e) == 1:
        break
    else:
        e += 2

d = pow(e, -1, phi)

C = pow(M, e, n)

M = pow(C, d, n)


print("n:", n)
print("Phi: ", phi)
print("d: ", d)
print("C: ", C)
print("M: ", M)
