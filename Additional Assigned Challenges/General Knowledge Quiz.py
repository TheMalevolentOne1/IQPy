"""
Create a general knowledge quiz persisting of 5 questions.
The quiz will not end until the 5 questions have been answered correctly.

Potentially Necessary Things:
String Manipulation
Arithmatic
While Loop
Inputs
If/Elif/Else Statements

plan:
while loop
question 1 through 5 with a variable for each making sure to put .lower()
if/elif/else statements for each question and answer



"""

score = 0
# I added above
while score < 5:
    question_1 = input("What is the Capital of England?").lower()
    if question_1 == "london":
        score += 1
    question_2 = input("What is the smallest country in Europe?").lower()
    if question_2 == "vatican city":
        score += 1
    question_3 = input("What is the most common surname in the United States?").lower()
    if question_3 == "smith":
        score += 1
    question_4 = input("Which planet has the most moons?").lower()
    if question_4 == "saturn":
        score += 1
    question_5 = input("What is the capital of France?").lower()
    if question_5 == "paris":
        score += 1
    print(f"You got {score}/5 correct!!")

    if score < 5:
        print("Wrong, try again")


# My Solution


"""
questions = ["Capital of England: ","Capital of France: "]
answers = ["London","Paris"]
score = 0

while score < 5:
    for i in range(len(questions)):
        userAns = input(f"{questions[i]}")
        
        if questions[i] == answers[i]:
            print("Correct")
            score += 1
        else:
            print("Wrong")
        
    print(f"You got {score} out of {len(questions)})
    
print("you got them all correct!")
"""
