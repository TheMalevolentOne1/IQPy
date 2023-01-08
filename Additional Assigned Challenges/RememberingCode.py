'''
Produce a program that will convert
ask user if they want to convert:
L to ML
or
ML to L

then ask for the value of L or ML they want to convert
then convert and print the converted value
"L to ML: convertedvalue"
"ML to L: convertedvalue"
L to ML

notes:
1L = 1000ML

must convert both ways.

requirements:
variables
if/elif/else statement
maths
'''
# I produced a solution if you get stuck reference it. If you copy it I will change the entire question.
#this good?
ml_or_l = input("L to ML or ML to L")
number = int(input("What number would you like converting?"))
if ml_or_l == ("ml to l"):
    print(f"result: {number / 1000}")
elif ml_or_l == ("l to ml"):
    print(f"result: {number * 1000}")
else:
    print("Invalid Value, try again!")

'''
next thing to do

Write a program that:
• asks the user their name
• if it is the same as your name, outputs
'You’re cool', otherwise outputs 'Nice to meet you'

Variables
If/Else Statement
'''
name = input("What is your name?").lower()
if name == "akos":
    print("You're cool")
else:
    print("Nice to meet you")
# :) :)

'''
Write a program that:
• asks the user their name
• asks what their favourite subject is
(using their name in the question)

IF the user likes the same subject that you do
say I love that subject too
if you don't 
response accordingly

Variables
'''

name = input("What's your name?")
favsub = input(f"What's your favourite subject, {name}?").lower()
if favsub == "science":
    print("OMG BESTIE MINE TOOOOO") # so gay.
elif favsub == "geography":
    print("I HATE YOUR SOUL") # same that lesson suckkkkkkeddddddd I HATE IT WITH A BURNING PASSIONHSUDUIAHDSADGSUIADHASHDUSAHUIDHSAIDUJSIAHDUISHDYUGYUDGSAYSUDG
else:
    print("oh right cool")