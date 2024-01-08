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


#TODO: 1. Print Report
def get_report():
    print("water: {}ml\nMilk: {}ml\nCoffe: {}g".format(resources["water"], resources["milk"], resources["coffee"]))
#TODO: 2. Check sufficient resources
def check_order():
    for ingredient in order_ingredients["ingredients"]:
        print(ingredient)
#TODO: 3. Process coins
#TODO: 4. Check transaction successful
#TODO: 5. Make Coffe
order = input("What would you like? (espresso/latte/capuccino)")
if order.lower() == "report":
    get_report()

try:
    order_ingredients = MENU[order]
    print("that will be ${}".format(order_ingredients["cost"]))
except KeyError:
    print('sorry that\'s not on the menu')

amount = float(input("enter cash: "))
def check_order():
    if amount >= order_ingredients["cost"] :
        ingredients = order_ingredients["ingredients"].values()
        for ingredient in ingredients :
            print(ingredient)
        #print("Here is your {}".format(order))

check_order()