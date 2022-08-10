from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.initial_pos()
        self.limit = FINISH_LINE_Y

    def pos_restart(self):
        self.initial_pos()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def initial_pos(self):
        self.clear()
        self.goto(STARTING_POSITION)
