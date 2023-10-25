##################################################################
# This Program will create milt to km converter app using tkinter
##################################################################

from tkinter import *  # type: ignore [reportWildcardImportFromLibrary]


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# creating mile input widget
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Creating Miles Label
mile_label = Label(text='Miles')
mile_label.grid(column=2, row=0)

# is equal label
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

# kilometer result lable
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Km label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
