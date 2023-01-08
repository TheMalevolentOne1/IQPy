'''
Write a game that:
• allows the user to play rock, paper,
scissors against the computer
• must display the computer’s choice
and show the result of the game

The computer's decision must be random

Variables
If/Elif/Else
Random Library
'''

import random

ai_answers = ["rock", "paper", "scissors"]

user_ans = input("Rock Paper or Scissors?").lower()
ai_ans = random.choice(ai_answers)

if user_ans == ai_ans:
    print("draw, try again")
elif user_ans == "rock" and ai_ans == "paper":
    print("you lost, computer picked paper")
elif user_ans == "paper" and ai_ans == "scissors":
    print("you lost, computer picked scissors")
elif user_ans == "scissors" and ai_ans == "rock":
    print("you lost, computer picked rock")
elif user_ans == "rock" and ai_ans == "scissors":
    print("you won, computer picked scissors")
elif user_ans == "paper" and ai_ans == "rock":
    print("you won, computer picked rock")
elif user_ans == "scissors" and ai_ans == "paper":
    print("you won, computer picked paper")
else:
    print("Incorrect value, try again")