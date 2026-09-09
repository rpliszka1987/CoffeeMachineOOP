from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_on = True
coffee_maker = CoffeeMaker()
machine_money = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What do you want to do? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        machine_money.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)