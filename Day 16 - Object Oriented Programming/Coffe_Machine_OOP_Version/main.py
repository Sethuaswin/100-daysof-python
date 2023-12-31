from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1. Printing the report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# TODO: 2. Check the resources are suffecirnt
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink)\
                and money_machine.make_payment(drink.cost):  # pyright: ignore
            # [reportOptionalMemberAccess]
            coffee_maker.make_coffee(drink)
