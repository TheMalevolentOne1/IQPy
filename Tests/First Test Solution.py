'''
You are NOT allowed to use any notes
You MUST either return this test through discord or the GitHub.
'''

'''
Produce a program to ask a user to enter a password and check for the following requirements:
Must have a capital letter AS THE FIRST LETTER
Must have numbers
Must be between 8 and 15 characters
Note: do not account for the possibility of a user having spaces in their password

If it meets the following then say the password is accepted
if it is missing ANY of the above criteria then say it is not accepted and what it is MISSING

--PERMITTED NOTES--:

example_string = "hello world"

print(example_string.count("hello"))
print(example_string.replace("world", "WORLD"))
print(len(example_string))


# isalpha Method - checks if the entire string is only the letters a-z no special case letters

example_isalpha_string = "Hello"

print(example_isalpha_string.isalpha()) #-> true


# isalnum Method - checks if the string is alphanumeric - letters a-z OR numbers 0-9 OR BOTH

print(example_isalpha_string.isalnum()) #-> true

example_isalnum_string = "Hello 12"

print(example_isalnum_string.isalnum()) #-> false

# Special Characters Including spaces are NOT alphanumeric so the value returned is false


example_string.istitle() -> checks if the string is a title type

example_string[0].isupper() -> true 

print(example_string[0]) -> the first letter of the example_string
'''

password = str(input("Enter a password: "))

if len(password) >= 8 and len(password) <= 15:
    if password[0].isupper():
        if not password.isalpha():
            print("Password Is Accurate")
        else:
            print("Must contain letters and numbers")
    else:
        print("Must have the first letter as a capital")
else:
    print("Password must be between 8 and 15 characters")