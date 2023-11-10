##########################################################################
# 1. This class create food for the snake at random position
# 2. Once it's eaten by the snake it will refresh at random position again
#########################################################################

from turtle import Turtle
import random


class Food(Turtle):  # the Turtle is a Super class

    def __init__(self):
        super().__init__()  # Inherting attributes for Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
