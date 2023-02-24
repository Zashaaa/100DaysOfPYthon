from art import logo
print(logo)


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

num1 = int(input("What's your first number?: "))

for operation in operations:
    print(operation)

desired_operation = input("Choose your desired operation from de symbols above: ")
num2 = int(input("What's your second number?: "))
answer = operations[desired_operation](num1, num2)
print(f"{num1} {desired_operation} {num2} = {answer}")
