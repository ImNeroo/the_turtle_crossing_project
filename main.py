from turtle import Screen
import time
from player import Player
from cars import Cars


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = Cars()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True

while game_on:
    if len(cars.cars) < 2:
        cars.cars_move()
        cars.create_cars()

    time.sleep(0.1)
    screen.update()


screen.exitonclick()
