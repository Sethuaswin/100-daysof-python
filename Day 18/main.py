from turtle import Turtle, Screen
import random
import turtle
tim = Turtle()
# tim.shape('turtle')
# tim.color('red')
# tim.forward(100)
# tim.right(90)

# TODO: 1. Draw a Square in turtle object
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# TODO: 2. Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# TODO: 3. Draw a triangle, square, pentagon, hexagon, heptagon, octagon,
#  nonagon and decagon and change the color randomly

# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen"
# ]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# TODO: 4. Generate a random walk
# 1. Increase the thickness
# 2. Increase the speed
# directions = [
#     0,
#     90,
#     180,
#     270,
# ]
# tim.pensize(15)
tim.speed('fastest')

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# TODO: 5. Creating Random Color
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# TODO: 6 Make a SPirograph

# Solution - Own:
# for _ in range(250):
#     tim.color(random_color())
#     tim.circle(100.00)
#     tim.left(5)

# Solution - Lecturar
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
