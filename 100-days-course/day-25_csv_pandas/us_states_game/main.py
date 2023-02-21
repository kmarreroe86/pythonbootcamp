import turtle
import pandas as pa

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pa.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if "Exit" == answer_state:
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)  # t.write(row.state.item())


#     create csv with missing states
missing_states = set(all_states).difference(set(guessed_states))
missing_states_dataframe = pa.DataFrame(missing_states)
missing_states_dataframe.to_csv("missing_states.csv")

# screen.exitonclick()

# Get the mouse click coordinates
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)

# same as screen.exitonclick()
# turtle.mainloop()
