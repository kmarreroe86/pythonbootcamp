import random
from hangman_art import logo, hanstages 
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
print(f"Test: Chosen word is: {chosen_word}")

lives = 6
word_length = len(chosen_word)
display = []
for i in range(word_length):    # Range from 0 -> word_length excluded
    display.append("_") # Same as display += "_"

while "_" in display and lives > 0:
    print(display)
    print(hanstages[lives])
    guess = input("Guess a letter: ").lower()    

    if guess in display:
      print(f"You've already guessed {guess}")
      continue

    # for letter in chosen_word:
    is_letter_present = False
    for i in range(word_length): # Range from 0 -> word_length excluded
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
            is_letter_present = True
    
    if not is_letter_present:
      print(f"You guessed{guess}, that's not in the world. You lose a life.")
      lives -= 1
        

if lives == 0:
    print(hanstages[lives])
    print("You lose!")
else:
    print(display)
    print("You win!")
