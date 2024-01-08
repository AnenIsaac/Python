from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)
    
def counter_clockwise():
    turtle.left(10)

def clockwise():
    turtle.right(10)
    
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key = 'w', fun = move_forwards)
screen.onkey(key= 's', fun = move_backwards)
screen.onkey(key= 'a', fun = counter_clockwise)
screen.onkey(key= 'd', fun = clockwise)
screen.okay(key= 'c', fun = clear)
screen.exitonclick()