from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS = []

class CarManager:
    pass 

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.move_distance = 5
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(300, 900), random.randint(-250, 280))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)
        
    def move(self):
        self.forward(MOVE_INCREMENT)
        
    def make_cars(self, level):
        num_cars = level*10
        for i in range(num_cars):
            car = Car()
            CARS.append(car)
    
    