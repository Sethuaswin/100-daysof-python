import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 26/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("Day 26/us-states-game/50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",   # noqa
                                    prompt="What's another state name? ").title()  # noqa # pyright: ignore[reportOptionalMemberAccess]

    # TODO: If answer_state is one of the states in all the states of the 50_states  # noqa
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]  # noqa
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Day 26/us-states-game/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))  # pyright: ignore[reportGeneralTypeIssues]  # noqa
        t.write(answer_state)
