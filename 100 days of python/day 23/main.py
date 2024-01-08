import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from car_manager import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('white')
   

cars = []
game_is_on = True
level_passed = False
scoreboard = Scoreboard()
turtle = Player()

screen.listen()
screen.onkey(turtle.move_forward, "Up")
screen.onkey(turtle.move_backward, "Down")

while game_is_on:
    
    #Generate all cars off-screen according to the level
    for i in range(scoreboard.level*10):
        car = Car()
        cars.append(car)
    #Move all cars forward
    while level_passed is False:
        time.sleep(0.1)
        screen.update()
        for car in cars:
            car.move()
            if turtle.ycor() > 280: 
                scoreboard.increase_level()
                turtle.refresh()
            if turtle.is_player_near_car(cars) is True:
                game_is_on = False
                scoreboard.game_over()
            
            if cars[-1].xcor() < 50:
                break
        else:
            continue  # This is executed if the inner loop completes without a break
        
        break
        


screen.exitonclick