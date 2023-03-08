'''
Python Test 3 - Registration System

IF you feel we haven't covered a specific area of this, let me know.
Otherwise, I will not be answering any questions.

The Python Notes are NOT permitted.

File Handling Access Methods (NOT all of these MAY be necessary)
"a" - Append File
"x" - Create File
"w" - Write File
"r" - Read File


This test will consist of multiple activities.

This test MAY contain the following:
For/While Loops
Lists
Variables
Loops
Functions
Arithmetic Operators
File Handling

You will not receive any help at all during the test.
There are multiple ways of doing the test, try to think of logical solutions outside the box.
'''

'''
Please complete the activities below at the very bottom of the file.
'''

'''
Activity 1:
Ask for the following (if add user):
Username
Forename
Surname
'''

'''
Activity 2: # provided answer due to issues
Add Validation to the USERNAME. 
It must ensure that the username DOES NOT already exist in the file.
If the USERNAME does exist already; inform the user and have them enter a different one.
REPEATEDLY TO ASK FOR USERNAME until they enter one that does not already exist.
Ensure that the data IS NOT ADDED to the txt file UNTIL Above.
'''

'''
Activity 3:
Add to Activity 1 the following:
Ask for age.
Ask for Current Education Level
'''

'''
Activity 4:
Validate Current Education Level
Only the following is permitted:
High School
College
University
Other

If they fail to enter one of the above.
REPEATEDLY ask until they enter one of those values. # Note: As with activity 2 this line is suspended please ignore it.

If the user enters Other.
Ask what their education level is
'''

'''
Activity 5:
Add their information into a file(s)
ENSURE THAT "-RegistrationTest" IS IN THE NAME OF THE FILE
FAILING TO DO SO, WILL PROMPT INSTANT FAILURE.
'''
'''
Activity 6:
At the beginning of the code at a menu.
It must use a WHILE LOOP.
Ask Whether they want to:
Add a user
Remove a user
See all users
Quit

You can do the menu however you like.
However it MUST have those and ONLY those options.
'''

'''
Activity 7:
Create a way for a user to delete a user from the file.
'''

'''
Activity 8:
Add a way to show all users in the file.
'''

'''
Activity 9
Add quit functionality.
'''

'''
Note: 
DO NOT RUSH. Do each activity CAREFULLY.
You can make a plan, whether physically drawn or notes written in a comment.
Any physical planning will need to be sent over Discord/WhatsApp for GitHub.
'''
'''
plan: 
split when reading from a file .split(" ")

'''

# Start Test Below

# activity 1 + past surname activity 3
username = input("Username: ")
forename = input("Forename: ").title()
surname = input("Surname: ").title()
age = int(input("Age: "))
edu_lvl = input("Current Education Level: ").title()
'''
#activity 2
file = open("data", "w")
file.write(username)
'''

# As dictated this activity 2 has been suspended until further notice.
# Added Help Below:
# check user
# read file contents
# SEPARATE the data into an array
# check IF the username EXISTS in a FOR LOOP
# if you think you can't do this at all under any conditions leave this activity and we will come back to it :)
# uhh okay ill leave it for now and we can get back to it



