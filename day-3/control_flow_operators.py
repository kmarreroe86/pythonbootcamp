print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride the rollecoaster")
    age = input("What is your age? ")
    if age > 18:
        print("Please pay $12")
    else: 
        print("Please pay $7")        
else:
    print("you cannot ride the rollecoaster")

# elif
if height >= 120:
    print("you can ride the rollecoaster")
    age = input("What is your age? ")
    if age < 12:
        print("Please pay $5.")    
    elif age <= 18:
        print("Please pay $7")
    elif age >= 45 and age <= 55:
        print("Everything it is gonna be ok. Have a free ride on us!")
    else: 
        print("Please pay $12")
else:
    print("you cannot ride the rollecoaster")

