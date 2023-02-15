from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

snake = []

for position in STARTING_POSITIONS:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake.append(new_segment)



screen.exitonclick()