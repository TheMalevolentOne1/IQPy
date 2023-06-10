'''
Challenge 26
Write a maths quiz with ten questions.
It must ask the user to input their name at
the start.
At the end it should display a message
informing the user of their score.
Write a function that saves the user’s
name and quiz result in a text file.

must add the first two numbers together and subtract the last one

You will need to use:
Variables
If/Elif/Else
CAN USE FOR LOOP AND A LIST :)
Functions
File Handling
'''
import random

name = input("Name: ").title()

score = 0

while score != 10:
    score = 0
    for i in range(11):
        num_1 = random.randint(1, 2)
        num_2 = random.randint(1, 2)
        num_3 = random.randint(1, 2)
        que = (num_1+num_2)-num_3 # 
        print(i)
        print(score)
        if que == (num_1+num_2)-num_3:
            score+=1

    print(f"You got a score of {score}")


