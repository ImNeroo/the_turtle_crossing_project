from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.current_score = 0
        self.write(f"Score: {self.current_score}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score: {self.current_score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
