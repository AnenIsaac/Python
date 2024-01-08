from turtle import Turtle
import random

ball = Turtle()
ball.shape('circle')
ball.penup()
ball.speed('normal')

def bounce():
    heading = 360 - ball.heading()

game_is_on = True
heading = random.randint(0, 360)
ball.heading(heading)
while game_is_on:
    ball.forward(10)
    if ball.xcor() > 280 or ball.xcor() < -280:
        heading = ball.heading()
        if 0 <= heading <= 180:
            new_heading = 180 - int(heading)
            ball.heading(new_heading)
            
        if 180 < heading <= 270:
            new_heading = heading + 90
            
        if 270 < heading < 360:
            new_heading = heading - 90