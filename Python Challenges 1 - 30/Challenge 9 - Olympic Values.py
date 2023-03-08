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
'''
olympic_value = input("Please enter one of the Olympic Values: ").lower()
if olympic_value == "respect" or olympic_value == "excellence" or olympic_value == "friendship":
    print("That's correct")
else:
    print("Try again")   
    
'''

# Added of list and for loop (New Code 02/03/2023) Below:
'''
Requirements:
For Loop
List
If/Elif/Else (May not be exactly as described)
'''

value = input("Please enter one of the Olympic Values: ").lower()
olympic_values = ["respect", "excellence", "friendship"]

for i in olympic_values:
    if value == i:
        print("That's correct")
        break
    else:
        print("Try again")