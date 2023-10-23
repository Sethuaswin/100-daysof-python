from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# TODO 1: Create and Move the turtle with keypress


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """
        Moving the turtle forward 10 basis points
        """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finisih_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
