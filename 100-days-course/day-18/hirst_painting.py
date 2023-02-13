# import colorgram
# import os
import turtle as turtle_module
import random


# rgb_colors = []
# colors = colorgram.extract('/Users/kmarrero/Documents/study/python/pythonbootcamp/100-days-course/day-18/image.jpg', 30)
# for color in colors:
#     rbg_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rbg_color)

# print(rgb_colors)

rgb_colors_from_image = [(212, 218, 228), (219, 168, 74), (220, 209, 216), (218, 212, 206), (210, 218, 213), (102, 177, 212), (230, 55, 93), (62, 91, 182), (156, 51, 111), (240, 81, 36), (218, 121, 198), (14, 109, 44), (27, 138, 112), (247, 148, 207), (79, 159, 44), (212, 212, 71), (13, 37, 139), (123, 13, 31), (173, 187, 178), (251, 164, 136), (60, 103, 202), (211, 212, 40), (189, 185, 206), (106, 12, 28), (181, 199, 186), (193, 71, 47), (10, 25, 101), (160, 203, 215), (12, 79, 27), (82, 147, 160)]
NUMBER_OF_DOTS = 101

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()


tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dots_count in range(1, NUMBER_OF_DOTS):
    tim.dot(20, random.choice(rgb_colors_from_image))
    tim.forward(50)
    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
