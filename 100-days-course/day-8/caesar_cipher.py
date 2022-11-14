from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo + "\n")

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  shift_amount = shift_amount % 26

  if cipher_direction == "decode":
      shift_amount *= -1

  for character in start_text:
    if character in start_text:
        position = alphabet.index(character)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += character
    
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


restart = "yes"
while "yes" == restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again \n").lower()

print("Goodbye")