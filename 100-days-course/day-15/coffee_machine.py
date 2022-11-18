from main import MENU, resources


TURN_OFF = "off"
REPORT = "report"

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"


def print_report(machine_resources):
    print(f"Water: {machine_resources['water']}")
    print(f"Milk: {machine_resources['milk']}")
    print(f"Coffee: {machine_resources['coffee']}")
    print(f"Money: {machine_resources['money']}")


def are_enough_resources(coffee, machine_resources):
    has_milk = "milk" in coffee["ingredients"]
    enough_water_and_coffee = (machine_resources["water"] >= coffee["ingredients"]["water"] and
            machine_resources["coffee"] >= coffee["ingredients"]["coffee"])
    
    return enough_water_and_coffee and machine_resources["milk"] >= coffee["ingredients"]["milk"] if has_milk else enough_water_and_coffee


def print_resources_lacking(coffee, machine_resources):
    has_milk = "milk" in coffee["ingredients"]
    if machine_resources["water"] >= coffee["ingredients"]["water"]:
        print("Sorry there is not enough water")
    if has_milk and machine_resources["milk"] >= coffee["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
    if machine_resources["coffee"] >= coffee["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")


def compute_change(coffee_cost, total_money):
    change = round(total_money - coffee_cost, 2)
    print(f"Here is ${change} dollars in change.")


def make_coffee(coffee, machine_resources, coffee_name):
    has_milk = "milk" in coffee["ingredients"]
    machine_resources["water"] = machine_resources["water"] - coffee["ingredients"]["water"]
    if has_milk:
        machine_resources["milk"] = machine_resources["milk"] - coffee["ingredients"]["milk"]
    machine_resources["coffee"] = machine_resources["coffee"] - coffee["ingredients"]["coffee"]
    print(f"Here is your {coffee_name.upper()}. Enjoy!")



def turn_on():
    machine_resources = resources

    coffee_option = "init"
    while True:

        coffee_option = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()

        if TURN_OFF == coffee_option:
            return

        if REPORT == coffee_option:
            print_report(machine_resources)
            continue

        coffee = MENU[coffee_option]

        if not are_enough_resources(coffee, machine_resources):
            print_resources_lacking(coffee, machine_resources)
            continue

        print(f"{coffee_option} costs: {coffee['cost']}")
        quarters = int(input("Insert how many quarters: "))
        dimes = int(input("Insert how many dimes: "))
        nickles = int(input("Insert how many nickles: "))
        pennies = int(input("Insert how many pennies: "))
        total_money_inserted = quarters * QUARTERS + dimes * DIMES + nickles * NICKLES + pennies * PENNIES
        if total_money_inserted < coffee["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue

        machine_resources["money"] += coffee["cost"]

        if total_money_inserted > coffee["cost"]:
            compute_change(coffee["cost"], total_money_inserted)

        make_coffee(coffee, machine_resources, coffee_option)


turn_on()
