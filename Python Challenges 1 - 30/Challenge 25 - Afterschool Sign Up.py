'''
Challenge 25
Write a sign-up program for an after school club; it should ask the user for the
following details and store them in a file:
• First Name
• Last Name
• Biographical Gender
• Year

You will need to use:
While Loop
Variables
File Handling
'''
#lst_file = open("scores", "r").read(-1).split("\n")

print("Hello World".split(" "))

while True:
    menu = int(input("What would you like to do? \n 1) Add to file \n 2) Read file \n 3) Delete a line \n 4) Quit Program"))
    if menu == 1:
        f_name = input("First Name: ").title()
        l_name = input("Last Name: ").title()
        gender = input("Biological Gender: ").title()
        year = int(input("Year: "))

        if year <= 11 and year >= 7:
            if gender == "Male" or gender == "Female" or gender == "Intersex":
                file = open("AfterSchoolClub", "a")
                file.write(f"First Name: {f_name}\nLast Name: {l_name}\nGender: {gender}\nYear: {year}\n")
                file.close()
            else:
                print("Incorrect Gender was found, please try again.")
        else:
            print("go away babies and grown ass men")
    elif menu == 2:
        file = open("AfterSchoolClub", "r")
        file_contents = file.read(-1)
        print(file_contents)
    elif menu == 4:
        quit()
    else:
        print("try again")