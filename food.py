from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Blue")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

