from tkinter import *  # type: ignore
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #  # noqa


# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # noqa
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = user_name_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")  # noqa
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"  # noqa
                                                                f"\nPassword: {password}\nIs it ok to save")  # noqa

        if is_ok:

            with open("Day 29/password-manager/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# ------------- window Setup ----------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# -------------- Canvas Setup --------------- #
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day 29/password-manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# -------------- Label Setup------------------ #
# Website Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Email/Username Label
user_name_label = Label(text="Email/Username:")
user_name_label.grid(row=2, column=0)

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ---------------- Entry Setup ---------------- #
# Website Input
website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# User Name/Email Input
user_name_input = Entry(width=52)
user_name_input.grid(row=2, column=1, columnspan=2)
user_name_input.insert(END, "example@something.com")

# Password Input
password_input = Entry(width=33)
password_input.grid(row=3, column=1)

# ---------------- Button Setup --------------- #
# Add button
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Generate Password Button
gen_pwd_button = Button(text="Generate Password", command=generate_password)
gen_pwd_button.grid(row=3, column=2)

window.mainloop()
