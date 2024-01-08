from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
        
    def move_backward(self):
        self.forward(-MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)
        
    def is_player_near_car(self, cars):
        for car in cars:
            if self.distance(car) < 20:
                return True
        return False