'''
You are NOT allowed to use any notes
'''

'''
PRODUCE a program that will ask the user for the following criteria:
Their forename,
Their surname,
Their date of birth,
Their Age (do not ask) (This MUST be calculated from their date of birth depending when they had their birthday)
Their phone number (must have a maximum number of numbers (this is up to you))

This data provided must be stored in the data_array.

You are provided the following:
Imported time
the empty array which MUST contain the data 
question asking if their birthday has already passed.

all datatypes must be accurate
Names - Strings
Dates - Strings with dd/mm/yyyy (Slashes can not be integers :P) 
Phone numbers - Ints
Ages - ints

The sections on validation or already written areas MUST NOT BE REMOVED.

The data MUST follow the ORDER PROVIDED as in the criteria.

UPDATED RULE CHANGE:
You may access the Arrays Notes for this examination
'''

'''
plan:
forename code
surname code
date of birth
age (use 29/12/2022 for date to check)
phone number (11 max)
'''
import test_validation as validate
import time

data_array = [] # input all final data in here for exam validation

forename = input("Forename?")
surname = input("Surname?")
day = int(input("Day of Birth?"))
month = int(input("Month of Birth?"))
year = int(input("Year of Birth?"))
# Code added before exam
birthday_passed = str(input("Has your birthday already passed?: ")).title()
validate.validate_birthday_state(birthday_passed)
# Code added before exam

if birthday_passed == "Yes":
    age = time.localtime().tm_year - year
else:
    age = (time.localtime().tm_year - 1) - year

print(f"Your age: {age}")

#what else is there in ze code thats it lol

phone_number = input("Please enter the phone number: ")
len_phone_number = len(phone_number)

# You need to make the birthday into the dd/mm/yyyy format :)

dobformat = f"{day}/{month}/{year}"

data_array.append(forename)
data_array.append(surname)
data_array.append(dobformat)
data_array.append(phone_number)

validate.validate_first_exam(data_array)