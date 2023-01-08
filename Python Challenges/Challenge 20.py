'''
Write a program that:
• asks the user to input a number and
repeats until they guess the number 7
• congratulate the user with a ‘Well
Done’ message when they guess correctly

Variables
While Loop
'''
user_num = int(input("Guess the number I'm thinking of"))
while user_num != 7:
    user_num = int(input("Guess again!"))
if user_num == 7:
    print("Well Done!")