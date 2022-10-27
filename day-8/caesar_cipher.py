from operator import le


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift):
    if shift > 25:  # 25 -> fixed alphabet length
        shift = shift % 26

    cipher_text = ""
    for letter in plain_text:
        idx = alphabet.index(letter)
        if idx + shift > 24:
            cipher_text += alphabet[(idx + shift) % 26]
        else:
            cipher_text += alphabet[idx + shift]

    return cipher_text


def decrypt(encrypted_text, shift):
    plain_text = ""
    
    for letter in encrypted_text:
        idx = alphabet.index(letter)
        plain_text += alphabet[idx - shift]
        # if idx - shift < 0:
        #     plain_text += alphabet[(idx + shift) % 26]
        # else:
        #     plain_text += alphabet[idx - shift]

    return plain_text

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
while "decrypt" == direction or "encrypt" == direction:
    result = ""
    if "decrypt" == direction:
        result = decrypt(text, shift)
    elif "encrypt" == direction:
        result = encrypt(text, shift)

    print(f"{result}")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
# encrypted = encrypt(text, shift)
# print(f"{encrypted}")