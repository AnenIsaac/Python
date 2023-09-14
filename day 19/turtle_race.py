from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="What colour turtle will win the race?")

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtles = []

def create_turtles(colours: list, turtles: list):
    for color in colours:
        var = color
        color = Turtle()
        color.color(var)
        color.shape('turtle')
        turtles.append(color)
    
def set_up_race(turtles: list):
    x = -230
    y = -170
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x, y)
        y += 50

def move_random_turtle():
    mover = random.choice(turtles)
    steps = random.randint(0, 10)
    mover.forward(steps)
    global winner 
    winner = mover
    return is_turtle_finished(mover)
    
def is_turtle_finished(turtle):
    if turtle.xcor() > 200:
        winner = turtle
        return False
    else:
        return True
        return True
    
create_turtles(colours, turtles)
set_up_race(turtles)
while move_random_turtle():
    pass

winner_color = winner.color()[0]
if user_bet.lower() == winner_color.lower():
    print(f"You Won! The winner was {winner_color}.")
else:
    print(f"You Lost! The winner was {winner_color}.")

screen.exitonclick()