from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", False, align=ALIGNMENT, font =FONT)
        self.hideturtle()
        
    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, align=ALIGNMENT, font =FONT)