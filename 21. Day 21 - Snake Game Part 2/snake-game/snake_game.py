############################################################################
# Running the Snake Game by,
# Calling the methods and attributes for snake.py file
###########################################################################

from turtle import Screen

from scoreboard import Scoreborad
from snake import Snake
import time
from food import Food

screen = Screen()
# Setting the screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreborad()

# Assigning the keys for the key strokes
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: 4. Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO: 6. Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -310 or snake.head.ycor() < -290 or snake.head.ycor() > 310:   # noqa
        game_is_on = False
        scoreboard.game_over()

    # TODO : 7. Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
