import turtle as t
import random

pointer = t.Turtle()
pointer.speed('fastest')
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    num = int(360/size_of_gap)
    for _ in range(num):
        pointer.color(random_color())
        pointer.circle(50)
        pointer.setheading(pointer.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()