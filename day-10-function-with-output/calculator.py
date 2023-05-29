from logo import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("Pick first number: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operator_symbol = input("Pick an operation: ")
        calculation_function = operations[operator_symbol]
        num2 = float(input("Pick an number: "))
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")
        continue_operation = input(f"Type 'y' to continue operations and 'n' to stop operations: ")

        if continue_operation == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
