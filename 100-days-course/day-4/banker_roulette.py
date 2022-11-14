# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


random_choice = random.randint(0, len(names) - 1)

print(f"{names[random_choice]} is going to buy the meal today!")

# print(len(names_string)) Prints length of the string

# =================================
# Random access list 2
print(f"{random.choice(names)} is going to buy the meal today!")
