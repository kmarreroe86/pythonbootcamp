import random

world_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(world_list)
print(f"Test: Chosen word is: {chosen_word}")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_length = len(chosen_word)
display = []
for i in range(word_length):    # Range from 0 -> word_length excluded
    display.append("_") # Same as display += "_"

# print(display)
# print(stages[lives])
while "_" in display and lives > 0:
    print(display)
    print(stages[lives])
    guess = input("Guess a letter: ").lower()    

    # for letter in chosen_word:
    is_letter_present = False
    for i in range(word_length): # Range from 0 -> word_length excluded
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
            is_letter_present = True
    
    if not is_letter_present:
        lives -= 1
        

if lives == 0:
    print(stages[lives])
    print("You lose!")
else:
    print(display)
    print("You win!")
