from turtle import Turtle, Screen
import random


# Configuration
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()


# Initialization
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_COORD = [-100, -50, 0, 50, 100, 150]
turtles_hit = []

for idx in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(COLORS[idx])
    new_turtle.goto(x=-230, y=Y_COORD[idx])
    turtles_hit.append(new_turtle)


# Race
is_race_on = True if user_bet in COLORS else False
while is_race_on:
    for turtle in turtles_hit:
        disatance = random.randint(0, 10)
        turtle = random.choice(turtles_hit)
        turtle.forward(disatance)
    
    if turtle.xcor() > 230:
        is_race_on = False
        winning_color_turtle = turtle.pencolor()

        if user_bet == winning_color_turtle:
            print(f"You've won! The {winning_color_turtle} turtle is the winner!")
        else:
            print(f"You've lost! The {winning_color_turtle} turtle is the winner!")



# Exit
screen.exitonclick()
