from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball(225)
r_score = Scoreboard((50, 250))
l_score = Scoreboard((-50, 250))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down") 
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move(5)
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        l_score.add_point()
        ball.restart()
        
    if ball.xcor() < -380:
        r_score.add_point()
        ball.restart()
        
    

screen.exitonclick()