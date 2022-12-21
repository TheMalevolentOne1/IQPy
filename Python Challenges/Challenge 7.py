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
tv_hours = int(input("How many hours do you watch TV per day?"))
if tv_hours < 2:
    print("That shouldn't rot your brain too much")
elif tv_hours < 4:
    print("Aren't you getting square eyes?")
else:
    print("Fresh air beats channel flicking")