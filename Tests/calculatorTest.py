'''
You must make:
Add
Subtract
Divide
Power
Times

These all must have separate Functions

This must be in an infinite While Loop (you can use while notes)

The user must decide what they want to select on the calculator

you must ask how many numbers they want to use the arithmetic method on (e.g: how many numbers do you want to divide)

The user can select a different equation they may want to do, in the event otherwise quit(this function is included)

Good Luck
'''
'''
Plan:
SEPARATE FUNCTIONS SEPARATE FUNCTIONS
infinity loop
how many numbers needed
ask the user for what they'd like to do e.g. / * - + and powers
how many numbers do you want to divide
if they want to do it again or quit

Help Notes I should NOT have given:
# plan example. Ask user -> ask number of numbers -> trigger needed function -> ask what numbers they want (for loop) -> print result -> code starts again due to while loop (I'll leave this here to help)
# btw you can use numbers for the if statement 1) Add 2) Subtract 3) Times etc (Might make it easier for the if statements)

I added *nums and for loop for them 
'''
# Do not delete
import os


def quitFunc():  # Quit Function
    os.close()


# Start Below

def add(num1, num2):
    print(num1 + num2)
    return


def subtract(num1, num2):
    print(num1 - num2)
    return


def divide(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Can not divide by 0")
    return


def multiply(num1, num2):
    print(num1 * num2)
    return


def power(num1, num2):
    print(num1 ** num2)
    return


while True:
    selection = int(input("Which calculator function would you like to use?\n1) Add 2) Subtract 3) Divide 4) Multiply 5) Power 6) Quit"))
    if selection == 1:
        number1 = int(input("What two numbers do you want to add together?\n first:"))
        number2 = int(input(" second:"))
        add(number1, number2)
    elif selection == 2:
        number1 = int(input("What two numbers do you want to subtract?\n first:"))
        number2 = int(input(" second:"))
        subtract(number1, number2)
    elif selection == 3:
        number1 = int(input("What two numbers do you want to divide?\n first:"))
        number2 = int(input(" second:"))
        divide(number1, number2)
    elif selection == 4:
        number1 = int(input("What two numbers do you want to multiply together?\n first:"))
        number2 = int(input(" second:"))
        multiply(number1, number2)
    elif selection == 5:
        number1 = int(input("What two numbers do you want to power?\n first:"))
        number2 = int(input(" second:"))
        power(number1, number2)
    elif selection == 6:
        quit = input("Would you like to quit?\n Y/N").upper()
        if quit == "Y":
            quitFunc()
