###########################################################
# TODO: 5. Create a Scoreboard and Keep track of the Score
##########################################################

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreborad(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Opening the data file which stores the high score
        with open("Day 24/snake-game/data.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)   # noqa

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # writing back into the data file with updated high_score
            with open("Day 24/snake-game/data.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
