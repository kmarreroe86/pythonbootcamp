PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = [name.strip() for name in file.readlines()]

with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    letter_template = file.read()
    for name in names:
        new_letter = letter_template.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
