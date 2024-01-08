from turtle import Turtle

ALIGNMENT = 'RIGHT'
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-150, 250)
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font =FONT)
        self.hideturtle()
          
    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"level: {self.level}", False, align="left", font =("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align="center", font =("Arial", 24, "normal"))