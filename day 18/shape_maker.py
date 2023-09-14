from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

list = [3, 4, 5, 6, 7, 8, 7, 9, 10]
for x in list:
    draw_shape(x)
    

screen = Screen()
screen.exitonclick()