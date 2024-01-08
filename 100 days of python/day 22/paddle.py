from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position : tuple) -> None:
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.goto(position)

    #paddle movement
    def up(self):
        new_ycor = self.ycor() +20
        self.goto(self.xcor(), new_ycor)
        
    def down(self):
        new_ycor = self.ycor() -20
        self.goto(self.xcor(), new_ycor)
    
    

