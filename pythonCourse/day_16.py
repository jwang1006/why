from day_16_menu import Menu, MenuItem
from day_16_coffee_maker import CoffeeMaker
from day_16_money_machine import MoneyMachine


bobMaker = CoffeeMaker()
dollarMaker = MoneyMachine()
choicesChoices = Menu()

def takeOrder():
    while True:
        itemName = input(f"Right, then, what can I get you? On our menu, we have: {choicesChoices.get_items()}, what do you want?")
        item = choicesChoices.find_drink(itemName)
        if item!=False and bobMaker.is_resource_sufficient(item):
            break
    while True:
        if dollarMaker.make_payment(item.cost):
            break
    bobMaker.make_coffee(item)

def report():
    bobMaker.report()
    dollarMaker.report()



while True:
    person = input("Would you like to (1) order, or (2) receive a tax report today?")
    if person == "1":
        takeOrder()
    else:
        report()

