from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# TODO: 1. Setup the Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# TODO: 3. Creating another Paddle and move

# Intializing the r_paddle and l_paddle object from Paddle class
r_paddle = Paddle((350, 0))
l_padle = Paddle((-350, 0))

# Intializing the ball object from Ball class
ball = Ball()

# Intializing the scoreboard object from Scoreboard class
scoreboard = Scoreboard()

# Intiating event listeners method for assigning keys
screen.listen()

# Assinging "up" and "Down" keys for the up and down for the right paddle
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

# Assinging "w" and "s" for the up and down for the left paddle
screen.onkey(key="w", fun=l_padle.go_up)
screen.onkey(key="s", fun=l_padle.go_down)

# Looping the game till the game_is_on
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # TODO: 5. Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO: 6. Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_padle) < 40 and ball.xcor() < -320:  # noqa
        ball.bounce_x()

    # TODO: 7. Detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect l_paddel misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
