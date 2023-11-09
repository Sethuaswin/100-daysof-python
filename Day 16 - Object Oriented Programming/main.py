# from turtle import Turtle, Screen
# # Creating an Object from a Blueprint
# timmy = Turtle()
# print(timmy)

# # Calling the Methods of an object
# # Changing shape
# timmy.shape('turtle')
# # Changing color
# timmy.color("coral")
# # Move forward
# timmy.forward(100)


# my_screen = Screen()
# # Calling an attributes of an object
# print(my_screen.canvheight)  # canvheight is the attribute
# # This method will not close the window until user clicks
# my_screen.exitonclick()

# PrettyTable
from prettytable import PrettyTable

# Creating an object table from PrettyTable class
table = PrettyTable()
table.header = True

# Adding Pokemon Name column
table.add_column(
    "Pokemon Name",
    [
       "Pikachu",
       "Squirtle",
       "Charmander",
    ]
)

# Adding Type Column
table.add_column(
    "Type",
    [
        "Electric",
        "Water",
        "Fire",
    ]
)

# Left aligning the entire table
table.align = "l"

print(table)
