def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1/ n2

operators = {
                "+": add,
                "-": sub, 
                "*": mul, 
                "/": div,
            }

import second_art

def calculator():
    print(second_art.logo)
    continue_doing = True
    first = float(input("What's the first number?: "))

    while continue_doing:
        for key in operators:
            print(key)

        pick = input("Pick an operation: ")

        second = float(input("What's the next number?: "))

        result = operators[pick](first, second)
        print(f"{first} {pick} {second} = {result}")

        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if again == "y":
            first = result
        else:
            continue_doing = False
            print("\n" * 20)
            calculator()

calculator()