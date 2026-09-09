from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_on = True
coffee_maker = CoffeeMaker()
machine_money = MoneyMachine()
coffee_options = Menu()

coffee_maker.report()
machine_money.report()
