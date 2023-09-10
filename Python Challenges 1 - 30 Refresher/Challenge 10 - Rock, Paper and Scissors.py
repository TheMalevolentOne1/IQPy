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

ai_ans = ["rock","paper","scissors"]

user_ans = input("Rock, Paper or Scissors?").lower()

ran_ans = random.choice(ai_ans)