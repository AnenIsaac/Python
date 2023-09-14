import turtle as t
import random

pointer = t.Turtle()
options = [0, 90, 180, 270]
colours = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Cyan", "Magenta"]
pointer.pensize(10)
pointer.speed('fast')
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    
for _ in range(100):
    pointer.color(random_color())
    pointer.forward(30)
    pointer.setheading(random.choice(options))
    
screen = t.Screen()
screen.exitonclick()