# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightNumber = float(height)
weightNumber = float(weight)

bim = weightNumber / heightNumber ** 2

print(int(bim))
