from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_at_start_position()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_at_start_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return True if self.ycor() > FINISH_LINE_Y else False