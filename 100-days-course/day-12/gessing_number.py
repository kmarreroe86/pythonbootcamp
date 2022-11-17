#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from random import randint
from art import header

DIFFICULTY_HARD = 5
DIFFICULTY_EASY = 10

def set_number_of_guesses():
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy'or 'hard': ")
    return DIFFICULTY_EASY if difficulty == "easy" else DIFFICULTY_HARD

def play():
    print(header)
    answer = randint(1, 100)
    guesses = set_number_of_guesses()
    print(f"You have {guesses} attempts remaining to guess the number.")

    while not guess == answer:
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it. The answer was: {guess}")
            break
        
        guesses -= 1
        if guesses == 0:
            break

        if guess > answer:
            print("To high.")        
        else:
            print("To low.")
        print(f"You have {guesses} attempts remaining to guess the number.")

    if guesses == 0:
        print(f"You run out of guesses, you lose. The asnwer was {answer}")



play()
