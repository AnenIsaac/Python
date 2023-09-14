import colorgram 
import turtle as t 
import random 

colors = colorgram.extract('image.jpg', 12)
list = []

for x in colors:
    rgb = x.rgb
    r = rgb.r
    g = rgb.g 
    b = rgb.b 
    color_tuple = (r, g, b)
    print(color_tuple)
    list.append(color_tuple)
    
print(list)

colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), 
          (202, 142, 31), (115, 155, 171), (124, 79, 99), 
          (122, 175, 156), (229, 236, 239), (226, 198, 131), 
          (242, 247, 244)]

turtle = t.Turtle()
turtle.hideturtle()
t.colormode(255)
turtle.penup()

turtle.penup()
turtle.goto(-230, -230)

for x in range(10):
    for y in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.forward(50)
    turtle.goto(-230, -230 + (x+1)*50)

screen = t.Screen()
screen.exitonclick()