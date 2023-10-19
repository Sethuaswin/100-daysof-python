###################################################################
# This Program will build the Turtle Race Game
###################################################################
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# Changing the Screen Size
screen.setup(width=500, height=400)

# Bring the popup to make a bet on particular color turtle
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")  # noqa
color_list = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple'
]

all_turtles = []

# creating 6 turtles for different position
# with different colur in the color_list
y = -100
for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! the {winning_color} turtle is the winner")  # noqa
            else:
                print(f"You have lost! the {winning_color} turtle is the winner")  # noqa
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
