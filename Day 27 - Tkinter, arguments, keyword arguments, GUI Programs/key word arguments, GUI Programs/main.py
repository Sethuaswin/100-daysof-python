###################################################################
# This program is to walk through of tkinter module for custom GUI
###################################################################

from tkinter import *  # type: ignore [reportWildcardImportFromLibrary]


def button_clicked():
    print("Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Creating window object with TK Class which will create the widow
window = Tk()
# changing the title of window
window.title("My first GUI Program")
# changing the window size
window.minsize(width=500, height=300)
# Adding padding (extra space) around the window
window.config(padx=20, pady=20)


# Creating Label
my_label = Label(text="This is a label", font=("Arial", 24, "italic"))


# update the lable
my_label['text'] = "New Text"
my_label.config(text="New Text")
# To show the label on the screen
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Creating a button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Creating a new button
new_button = Button(text="New Button")
# button.pack()
new_button.grid(column=2, row=0)


# Getting input from the user which is 'Entry' method
input = Entry(width=10)
# Gets text in entry
print(input.get())
# input.pack()
input.grid(column=3, row=2)

# Warning!
# We can't mix with grid and pack() method

# mainloop() method will keep the window open
window.mainloop()
