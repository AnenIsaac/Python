from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.speed("slow")
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()
is_turtle_moving = True
while is_turtle_moving:
    time.sleep(0.1)
    for seg_num in range(2, 0, -1):
        print(seg_num)
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(10)

screen.exitonclick()
