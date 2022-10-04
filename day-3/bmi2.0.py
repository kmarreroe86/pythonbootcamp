# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
bmiResult = ""

if bmi < 18.5:
    bmiResult = "underweight"
elif bmi < 25:
    bmiResult = "normal weight"
elif bmi < 30:
    bmiResult = "slightly overweight"
elif bmi < 35:
    bmiResult = "obese"
else:
    bmiResult = "clinically obese"

print(f"Your BMI is {round(bmi)}, you are {bmiResult}")