from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.setheading(90)
    tim.forward(10)


def move_backwards():
    tim.setheading(270)
    tim.forward(10)


def turn_left():
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    
    # same as above
    tim.left(10) 
    tim.forward(10)
    

def turn_right():
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)

    # same as above
    tim.right(10)
    tim.forward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(clear, "c")
screen.exitonclick()