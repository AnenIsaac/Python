from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class State(Turtle):
    def __init__(self, name) -> None:
        super().__init__()
        self.score = 0
        self.name = name
        self.color("black")
        self.penup()
        self.goto(0, 250)
        self.write(f"{self.name}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def move_to(self, x, y):
        self.goto(x, y)
