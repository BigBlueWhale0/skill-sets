import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Game")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
screen.onkey(player.move, "Up")


car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    if player.ycor() >= 280:
        scoreboard.increase_score()
        player.go_to_start()
        car_manager.level_up()

screen.exitonclick()