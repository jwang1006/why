def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

basic_operations = {
    "*": multiply,
    "/": divide,
    "+": add,
    "-": subtract
}

from day_10_art import logo
print(logo)
num1 = float(input("What is first number?\n"))
for key in basic_operations:
    print(key)
operation = input("Which operation would you like to use?\n")
num2 = float(input("What is the second number?\n"))
function = basic_operations[operation]
answer = function(num1, num2)
print(f"{num1} {operation} {num2} = {answer}")
while True:
    continueCalculating = input(f"Type 'y' to continue with {answer}, or 'n' to finish.\n")
    if continueCalculating == "n":
        break
    for key in basic_operations:
        print(key)
    operation = input("Which operation would you like to use?\n")
    nextNum = float(input("What is the next number?\n"))
    function = basic_operations[operation]
    answer = function(answer, nextNum)
    print(f"{answer} {operation} {nextNum} = {answer}")
