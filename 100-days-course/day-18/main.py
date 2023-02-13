from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

# Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# figures
colors = ["Green", "Black", "IndianRed", "DarkOrchid", "SlateGray", "Blue", "CornflowerBlue", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for shape_sides in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_sides)


# Random walk
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fast")

# for _ in range(200):
#     timmy.color(random.choice(colors))
#     timmy.forward(50)
#     timmy.setheading(random.choice(directions))


# Spirograph
def random_Color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed("fast")
timmy.color(random_Color())
timmy.circle(100)

my_screen = Screen()
my_screen.exitonclick()