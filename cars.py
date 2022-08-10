from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.cars = self.all_cars[0:1]

    def create_cars(self):

            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-290, 290))
            self.all_cars.append(new_car)

    def cars_move(self):
        for square in range(0, len(self.all_cars) - 1):
            self.all_cars[square].forward(STARTING_MOVE_DISTANCE)
