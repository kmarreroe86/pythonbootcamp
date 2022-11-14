import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# print(rock + "\n" + paper + "\n" + scissors)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
choices = [rock, paper, scissors]

if player_choice > 2:
    print("You enter an invalida option")
else:
    computer_choice = random.randint(0, 2)
    print("You:" + choices[player_choice] + "\n")
    print("Computer:" + choices[computer_choice] + "\n")

    if player_choice == computer_choice:
        print("It is a draw")
    elif player_choice == 0 and computer_choice == 2:
        print("You win")
    elif player_choice == 0:
        if computer_choice == 1:
            print("You lose")
        else:
            print("You win")
    elif player_choice == 1:
        if computer_choice == 2:
            print("You lose")
        else:
            print("you win")
    elif player_choice == 2:
        if computer_choice == 0:
            print("You lose")
        else:
            print("You win")
