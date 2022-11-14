from global_art import calculator_logo

def add(n1: float, n2: float):
    return n1 + n2


def subtract(n1: float, n2: float):
    return n1 - n2


def multiply(n1: float, n2: float):
    return n1 * n2


def divide(n1: float, n2: float):
    if (n2 == 0):
        raise Exception("Divisor cannot be 0 undefined operation")
    else:
        return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def list_operations():
    for oper in operations:
        print(oper)

def calculator():
    num1 = float(input("Enter first number: "))

    should_continue = True
    while should_continue:
        list_operations()
        choosen_operation = input("Pick an operation from the line above: ")
        num2 = float(input("Enter second number: "))
        answer = operations[choosen_operation](num1, num2)
        print(f"{num1} {choosen_operation} {num2} = {answer}")

        if input(f"Type 'y' to continued calculating with {answer} or type 'n' to exit ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


print(calculator_logo)
calculator()
