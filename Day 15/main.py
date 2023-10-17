MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Check the resources are suffiencnt


def is_resources_sufficient(order_ingredients):
    """
    Retruns True when order can be made, False if ingredients are insufficient
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO: 2. Procee the User's coin and calculate total amount


def process_coines():
    """
    Returns the total calculates from the coins inserted
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO: 3. Check the transaction and return change if excess amount paid by
# the user and add the drink amount into the profit


def is_transactions_successful(money_received, drink_cost):
    """
    Return True when the payment is accepted, or False if money is insufficient
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enoigh money, Money refunded")

# TODO: 4 Make coffee based on the user choice and detuct in the resource


def make_coffee(drink_name, order_ingredients):
    """
    Detuct the required ingredients from the resources.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True


# TODO: 5 run on a while loop, take input from the user for the drink name,
# create report, and process coins, check transaction and resources


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccine): ")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coines()
            if is_transactions_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
