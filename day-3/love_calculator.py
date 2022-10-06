# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2;
combined_lower_names = combined_names.lower();
trueCounter = 0
loveCounter = 0

for letter in "true":
    trueCounter += combined_lower_names.count(letter);

for letter in "love":
    loveCounter += combined_lower_names.count(letter);

loveScore = trueCounter * 10 + loveCounter    #loveScore = int(str(trueCounter) + str(loveCounter))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}")