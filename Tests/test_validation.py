import re

def validate_first_exam(array):
    if len(array) == 0:
        print("You failed to input any user data into the array. Exam Failed.")
        return
    elif len(array) == 5:
        print("Array Missing data!")
        return
    if type(array[0]) == str:
        print("Forename DataType is correct")
        if type(array[1]) == str:
            print("Surname DataType is correct")
            if type(array[2]) == str:
                print("Date of birth DataType is the correct")
                if re.match(r"\d{1,2}\/\d{1,2}\/\d{4}", array[2]):
                    print("Date of birth follows the formatting of the exam")
                    if type(array[3]) == str:
                        print("Phone number is the correct datatype")
                        if len(str(array[3])) == 11:
                            print("The phone number is the correct length")
                            print("\nEverything is correct!")
                        else:
                            print("Phone Number is not 11 numbers")
                    else:
                        print("phone number is the wrong DataType")
                        return
                else:
                    print("The formatting of the Date Of Birth is incorrect.")
                    return
            else:
                print(f"Date Of Birth DataType is incorrect. Type: {type(array[2])}")
                return
        else:
            print(f"Surname DataType is incorrect. Type: {type(array[1])}")
            return
    else:
        print(f"Forename DataType is incorrect. Type: {type(array[0])}")
        return

def validate_birthday_state(ans):
    if ans not in ['Yes', 'No']:
        print("Answer must only be Yes or No!")
        return quit()
    else:
        print("Answer is within acceptable values :)")
        return