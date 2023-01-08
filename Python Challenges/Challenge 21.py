'''
Write a program that converts between centimetres, and inches and vice versa, by:
• asking the user to input a number
• asking the user to choose between
converting from centimetres to inches or from
inches to centimetres
• calculating and outputting the result using
functions

Additional Information:
1 inch= 2.54cm
1 cm = 0.393700787 inches

Variables
If/Elif/Else Statement
'''
# nice break he said, NICE BREAK HE SAID yes. All this is if/elif/else
num = int(input("What is the number?"))
# it makes things quicker to do
inch_or_cm = int(input("Would you like to convert 1) inch to cm 2) cm to inch?: "))
if inch_or_cm == 1:
    print(f"{num} inch = {num * 2.54} cm")
elif inch_or_cm == 2:
    print(f"{num} cm = {num * 0.393700787} inch")
else:
    print("Try again")