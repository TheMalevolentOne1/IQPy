'''
Write a program that:
• asks the user how long on average
they spend watching TV each day
• if it is less than 2 hours, outputs ‘That
shouldn’t rot your brain too much’; if it is less than 4 hours per day, outputs ‘Aren’t you getting square eyes?’;
otherwise outputs ‘Fresh air beats channel flicking’

Variables
If/Elif/Else Statement
'''
average = int(input("Average TV Hours per Day:"))
if average < 2:
    print("That shouldn’t rot your brain too much")
elif average < 4:
    print("Aren't you getting square eyes?")
else:
    print("Fresh air beats channel flicking")
# asks user for avg amount of time, and compares it to 2 hours and 4 hours of watch time
