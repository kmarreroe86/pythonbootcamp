# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 
# It will take your current age as the input and output a message with our time left in this format:
# > You have x days, y weeks, and z months left. 
# Where x, y and z are replaced with the actual calculated numbers. 

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_number = int(age)
remaining_years = 90 - age_as_number

x = remaining_years * 365
y = remaining_years * 52
z = remaining_years * 12
print(f"You have {x} days, {y} weeks, and {z} months left. ")