payment_received=0
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



def report():
    for i in resources:
     print(f"{i} : {resources[i]}")


def off():
    return False

def check_resources(required_resources):
    for i in required_resources:
        if required_resources[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def payment():
    print("Please Enter Coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many Dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total  = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    return total

def drinks(required_resources,drink_type):
    for i in required_resources:
        resources[i]=resources[i] - required_resources[i]
    print(f"Here is your {drink_type}, Enjoy")

def transaction(money_received,drink_name):
    if money_received >= MENU[drink_name]["cost"]:
        change = round(money_received-MENU[drink_name]["cost"])
        print(f"Here is your change: ${change}")

        return True
    else:
        print("Not Enough Money")
        return False


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == 'off':
        is_on = off()
    elif user_choice == 'report':
        report()
    else:
        if check_resources(MENU[user_choice]["ingredients"]):
            paytment_received = payment()
            if transaction(paytment_received,user_choice):
                drinks(MENU[user_choice]["ingredients"],user_choice)

