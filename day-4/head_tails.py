#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

# 1 - Head
# 0 - Tails

for n in range(10):
    random_val = random.randint(0, 1)
    if random_val == 0:
        print("Tails")
    else:
        print("Heads")

