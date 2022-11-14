#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

total_bil_str = input("What was the total bill? $")
tip_percentag_str = input("How much tip would you like to give 10, 12, or 15? ")
people_number_str = input("How many people to split the bill? ")

bill_as_number = float(total_bil_str)
tip_as_number = float(tip_percentag_str)
people_as_number = int(people_number_str)

total_to_pay = bill_as_number * (1 + tip_as_number / 100)
# splited_amount = round(total_to_pay / people_as_number, 2)
splited_amount = "{:.2f}".format(round(total_to_pay / people_as_number, 2))
print(f"Each person should pay: ${splited_amount}")