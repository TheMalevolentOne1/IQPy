'''
Write a program that:
• asks the user their name
• asks what their favourite subject is
(using their name in the question)
• responds to their answer by saying
that you like that subject as well

Variables
'''

name = input("What is your name?").title()
fav_subject = input(f"{name}, what is your favourite subject?")
print(f"i like {fav_subject} too")
