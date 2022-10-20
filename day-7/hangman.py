from operator import le
import random

world_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(world_list)
print(f"Test: Chosen word is: {chosen_word}")

display = []
for i in range(0, len(chosen_word) - 1):
    display.append("_")

guess = input("Guess a letter: \n").lower()

# for letter in chosen_word:
for i in range(0, len(chosen_word) - 1):
    letter = chosen_word[i]
    if letter == guess:
        display[i] = letter        

print(display)

# if guess in chosen_word:
#     print("correct")
# else:
#     print("incorrect")

