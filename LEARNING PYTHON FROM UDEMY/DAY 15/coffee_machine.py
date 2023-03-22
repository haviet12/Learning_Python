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
def test_resources(ingredients):
    enough=True
    for item in ingredients:
        if ingredients[item]>= resources[item]:
            print(f"Sorry there is not enough {ingredients[item]}.")
            enough = False
        return enough
    return enough
        
def process_coin():
    print("Please insert coins")
    total = int(input("How many quarter?: "))*0.25
    total += int(input("How many dime?: "))*0.1
    total += int(input("How many neckles?: "))*0.05
    total += int(input("How many penny?: "))*0.01
    return total

def transaction_successful(user_coin,drink_coin):
    if user_coin>=drink_coin:
        change_coin = round(user_coin - drink["cost"],2)
        print(f"Here is {change_coin} dollars in change.")
        global profit
        profit+= drink["cost"]
        return True
    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, ingridients):
    for item in ingridients:
        resources[item]-= ingridients[item]
    print(f"Here is your {drink_name}")
profit=0

active = True
while active:
    choosen = input("What would you like? (espresso, latte or cappuccino): ").lower()
    if choosen =='off':
        active=False
    elif choosen =='report':
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}ml')
        print(f'Water: {resources["water"]}ml')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choosen]
        if test_resources(drink["ingredients"]):
            user_coin=process_coin()
            if transaction_successful(user_coin=user_coin, drink_coin=drink["cost"]):
                make_coffee(drink_name=choosen,ingridients=drink["ingredients"])
