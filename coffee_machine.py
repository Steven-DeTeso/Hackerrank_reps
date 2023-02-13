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


def check_resources(drink_order) -> bool:
    """Takes in drink order as input, returns True if there are enough resources to make order, returns False if there isn't and prints what is missing"""
    is_enough = True
    for item in drink_order:
        if drink_order[item] > resources[item]:
            print(f"Sorry, there isn't enough {item} to make your order.")
            is_enough = False
    return is_enough

def report_resources() -> str:
    """When user enters 'report', func is called and outputs report statement"""
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${profit}"


def process_coins() -> int:
    """Returns the total calculated value from the input of coins."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(coins_inserted, drink_cost) -> bool:
    """Takes in payment and the cost of the drink. Returns True if the payment is enough and makes change, returns False if not enough money is entered"""
    if coins_inserted >= drink_cost:
        change = round(coins_inserted - drink_cost, 2)
        print(f"Here is the ${change} in change.")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


is_on = True

def make_coffee(drink_name, order_ingredients) -> str:
    """Takes in drink name ordered and its ingredients, deducts the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Please Enjoy!")

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        print(report_resources())
    else:
        drink = MENU[order]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(order, drink['ingredients'])