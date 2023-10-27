from cgitb import text
from email.mime import image
from tkinter import *  # type: ignore
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# --------------------- Data read and write --------------------------------- #
try:
    data = pd.read_csv("Day 31/flash-card-program/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Day 31/flash-card-program/data/french_words.csv")  # noqa
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
current_card = {}


# --------------------- Next Card ----------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# --------------------- Flip the card ------------------------------ #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# --------------------- Saving Prograss --------------------------- #
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("Day 31/flash-card-program/data/words_to_learn.csv", index=False)  # noqa
    next_card()


# --------------------- UI Setup ---------------------------------- #
# ----------------- Window Setup ----------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# ----------------- Canvas setup ------------------------ #
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="Day 31/flash-card-program/images/card_front.png")  # noqa
card_back_img = PhotoImage(file="Day 31/flash-card-program/images/card_back.png")  # noqa
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # noqa
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))  # noqa
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# ----------------- Button Setup ----------------------- #
# Cross Button
cross_image = PhotoImage(file="Day 31/flash-card-program/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)  # noqa
unknown_button.grid(row=1, column=0)

# Check Button
check_image = PhotoImage(file="Day 31/flash-card-program/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)  # noqa
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
