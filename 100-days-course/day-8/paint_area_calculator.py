#Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    wall_area = height * width
    number_of_cans = wall_area / cover
    return math.ceil(number_of_cans)
    






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
cans = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You will need {cans} cans of paint")