'''
Write a program that:
• asks the user to name one of the
Olympic Values (Respect, Excellence
and Friendship)
• if they correctly name one, output
'That’s correct‘, otherwise output 'Try again'

Variables
If/Elif/Else
'''
olympic_value = input("Please enter one of the Olympic Values").lower()
if olympic_value == "respect" or olympic_value == "excellence" or olympic_value == "friendship":
    print("That's correct")
else:
    print("Try again")