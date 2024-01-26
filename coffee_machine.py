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
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there are not enough {item}")
            return False
    return True
def process_coins():
    print("enter the coins")
    total=int(input("enter the no of quarter"))*0.25
    total+=int(input("enter the no.of dimes"))*0.1
    total+=int(input("enter the no.of nickle"))* 0.05
    total+=int(input("enter the no.of pennies"))*0.01
    return total
def is_transaction_successful(money_recived,drink_cost):
    if money_recived>=drink_cost:

        change=round(money_recived-drink_cost,2)
        print(f"here is ${change} in change")
        global profit
        profit +=drink_cost
        return True
    else:
        print("sry you didn't have enough money")
        return False
def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name}")
is_on=True
while is_on:
    choice=input("enter your choice espresso/latte/cappuccino")
    if choice =="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}g")
        print(f"money=${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])