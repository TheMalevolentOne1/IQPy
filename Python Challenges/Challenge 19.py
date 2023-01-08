'''
Write a program that:
• asks the user to input a number
• outputs the times table for that
number
• starts again every time it finishes

Variables
While Loop
For Loop
'''


while True:
    num = int(input("What is the number?"))
    for i in range(1, 11):
        print(f"{i} * {num} = {i*num}")
