'''
Exercise 1:
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
'''
import time

import datetime
year = datetime.date.today().year

name = input("Name:")
age = int(input("Age:"))
hbby = input("Has it been your birthday yet?").lower()
if hbby == "no":
    year -= 1
    print(f"Name: {name} \n Age: {age} \n You will be 100 years old in year {(year - age) + 100}")
elif hbby == "yes":
    print(f"Name: {name} \n Age: {age} \n You will be 100 years old in year {(year - age) + 100 }")
else:
    print("incorrect value, try again.")
'''

'''
Exercise 2:
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user.
(Clue: %)

'''
#num = int(input("Number:"))
#if num % 2 == 0:
#    print("Wow, a very even value")
#else:
#    print("That's quite an odd value")

'''
Exercise 3:
Make a two-player Rock-Paper-Scissors game. (again. For basic remembrance)

extension:

add scoring
'''
while True:
    plr1choice = input("Player One Choice:").lower()
    plr2choice = input("Player Two Choice:").lower()
    if plr1choice == "rock" and plr2choice == "rock":
        print("Draw")
    elif plr1choice == "paper" and plr2choice == "paper":
        print("Draw")
    elif plr1choice == "scissors" and plr2choice == "scissors":
        print("Draw")
    elif plr1choice == "rock" and plr2choice == "paper":
        print("Player 2 Wins!")
    elif plr1choice == "rock" and plr2choice == "scissors":
        print("Player 1 Wins!")
    elif plr1choice == "paper" and plr2choice == "rock":
        print("Player 1 Wins!")
    elif plr1choice == "paper" and plr2choice == "scissors":
        print("Player 2 Wins!")
    elif plr1choice == "scissors" and plr2choice == "rock":
        print("Player 2 Wins!")
    elif plr1choice == "scissors" and plr2choice == "paper":
        print("Player 1 Wins!")
    else:
        print("Incorrect value, try again")






'''
Exercise 4:
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number.
Then tell them whether they guessed too low, too high, or exactly right.
Continue until they guess correctly
'''

'''
Exercise 5:
Try to program a hangman game. 
(Remember: hello = "Hi" and print(hello[0]) = H)
'''

