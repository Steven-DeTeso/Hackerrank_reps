from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()

menu = Menu()

money_machine = MoneyMachine()


is_on = True 

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ")
    if order == 'off':
        is_on = False
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    else: 
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
                