from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font =FONT)
        self.hideturtle()
          
    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font =("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align="center", font =("Arial", 24, "normal"))