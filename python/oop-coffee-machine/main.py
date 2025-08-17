from idlelib.mainmenu import menudefs

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

coffee_machine.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):  ")
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)





# coffee_machine.is_resource_sufficient(coffee.find_drink("latte"))