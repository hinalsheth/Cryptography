def caesar_cipher(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) + shift_amount - base) % 26 + base)
        else:
            result += char

    return result
