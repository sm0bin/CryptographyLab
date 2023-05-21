def ceaser(massage, shift):
    text = ""
    for ch in massage:
        if ch.isalpha():
            shiftChar = chr((ord(ch.upper()) - 65 + shift) % 26 + 65)
            if ch.islower():
                text += shiftChar.lower()
            else:
                text += shiftChar
        else:
            text += ch
    return text


print(ceaser("Hello mobin", 3))

print(ceaser("Khoor prelq", -3))
