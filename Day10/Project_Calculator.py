from art import logo


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": devide
}


def calculator():
    print(logo)
    num1 = float(input("What's your first number?: "))

    for operation in operations:
        print(operation)

    continue_calculating = True
    while continue_calculating:
        desired_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[desired_operation](num1, num2)
        print(f"{num1} {desired_operation} {num2} = {answer}")
        if input(f"Type 'y'to continue calculating with {answer}, or Type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            continue_calculating = False
            calculator()


calculator()
