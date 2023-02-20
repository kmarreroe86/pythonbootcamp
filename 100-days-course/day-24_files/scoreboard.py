from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = None
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.load_high_score_data()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score_data()
        self.score = 0
        self.update_scoreboard()

    def load_high_score_data(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def save_high_score_data(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

