###################################################################
# This program is to walk through of tkinter module for custom GUI
###################################################################

from tkinter import *  # type: ignore [reportWildcardImportFromLibrary]

# Creating window object with TK Class which will create the widow
window = Tk()
# changing the title of window
window.title("My first GUI Program")
# changing the window size
window.minsize(width=500, height=300)


# Creating Label
my_label = Label(text="This is a label", font=("Arial", 24, "italic"))

# To show the label on the screen
my_label.pack()

# update the lable
my_label['text'] = "New Text"
my_label.config(text="New Text")


# Creating a button
def button_clicked():
    print("Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()


# Getting input from the user which is 'Entry' method
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)  # noqa
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)  # noqa
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)  # noqa
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# mainloop() method will keep the window open
window.mainloop()
