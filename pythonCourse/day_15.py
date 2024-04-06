import time, os
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

def run():
    while True:
        person = input("Hello, there! Are you a customer, or an owner?\n")
        if person=="customer":
           orderDrink()
        else:
            getReport()
        os.system("clear")

def orderDrink():
    print("We have the following drinks on our menu: ")
    for drinkType in MENU:
        print(drinkType)
    selectedDrink = input("What would you like?\n")
    if not checkResources(selectedDrink):
        orderDrink()
        return
    makeDrink(selectedDrink)   
    handleChange(selectedDrink)


def checkResources(drinkType):
    for ingredientName in MENU[drinkType]["ingredients"]:
        if MENU[drinkType]["ingredients"][ingredientName]>resources[ingredientName]:
            return False
    return True

def makeDrink(drinkType):
    global money
    money+=MENU[drinkType]["cost"]
    for ingredientName in MENU[drinkType]["ingredients"]:
        resources[ingredientName]-=MENU[drinkType]["ingredients"][ingredientName]

def handleChange(drinkType):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    moneyGiven = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    if moneyGiven<MENU[drinkType]["cost"]:
        print("Not enough money. Refunding...")
        time.sleep(1)
        os.system("clear")
        handleChange(drinkType)
        return
    print(f"Here's your change: {moneyGiven-MENU[drinkType]["cost"]}")
    time.sleep(1)
    print(f"Here's your {drinkType} ☕")
    time.sleep(1)
    print("Thanks for coming!")
    time.sleep(1)

def getReport():
    print("Here's your report:")
    for key in resources:
        print(f"{key}: {resources[key]}ml")
        time.sleep(1)
    print(f"Money: {money}")
    time.sleep(1)
    print("Thanks for coming in!")

run()