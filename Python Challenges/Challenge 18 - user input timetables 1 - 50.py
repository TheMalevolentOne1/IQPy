'''
Write a program that:
• asks the user to input a number
• outputs the times table for that
number

times tables 1 - 50

Variables
For Loops
'''

number = int(input("which times table should be displayed?"))
for i in range (1, 51):
    print(f"{i} * {number} = {i*number}")

