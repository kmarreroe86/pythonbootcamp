from turtle import Turtle


# WIDTH = 20
# HIGH = 100


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        print("go_up")

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        print("go_down")
