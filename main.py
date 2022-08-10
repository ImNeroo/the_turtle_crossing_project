from turtle import Screen
import time
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True

car = Cars()
count = 0
level = 0
while game_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    if level < 5 and count % 6 == 0:
        car.create_car()
    elif level > 5 and count % 3 == 0:
        car.create_car()
    car.move_cars()
    # Detecta si el jugador colisiono con el carro
    for index in car.all_cars:
        if index.distance(player) < 20:
            score.game_over()
            game_on = False
    # Detecta si cruzó la carretera
    if player.is_at_finish_line():
        player.initial_pos()
        car.level_up()
        score.update_score()
        level += 1
screen.exitonclick()
