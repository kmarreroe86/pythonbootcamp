# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

totalBill = 0;
if "S" == size:
    totalBill = 15
elif "M" == size:
    totalBill = 20
else:
    totalBill = 25

if "Y" == add_pepperoni:
    if "S" == size:
        totalBill += 2
    else:
        totalBill += 3

if "Y" == extra_cheese:
    totalBill += 1

print(f"Your final bill is: ${totalBill}")
