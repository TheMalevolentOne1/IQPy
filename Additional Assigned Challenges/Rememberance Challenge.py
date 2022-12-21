'''
Create a program that will ask the user the following
Their name
Their age
Their number of friends

if friends < 5:


If/elif/else notes

IMPORTANT SYMBOLS
Symbol | English
!= - not equal to
== - is equal to
<= - greater then or equal to
>= - less than or equal to
> - less than
< - greater then

IMPORTANT KEY WORDS
and
or
not

EXAMPLES OF ABOVE

if 1 == 3:
    print("Hello World")
else:
    print("1 is not equal to 3")

English: if 1 is equal to 1 and 2 is equal to 2 then print Hello World
'''

name = str(input("What is your name?"))
age = int(input("How old are you?"))
number_of_friends = int(input("How many friends do you have?"))
print(f"Your name: {name}, your year of birth: {2022-age}")
if number_of_friends < 5:
    print("You have a little amount of friends")
