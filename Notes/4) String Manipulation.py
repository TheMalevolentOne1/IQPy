#String Concatenation

x = 100

print("Number: "+str(x)) #Converting one datatype to another is called Casting

# The example above: due to the + type of concatenation it can not add it to the string due to x being an int value



#Does not add a space to the end of the string

print("Number:",x)

#Adds a space on the end of the string

print(f"Number: {x}")

#Easiest way to control the formatting of the string (does not require casting)


#Beginnings of String Manipulation

"".title() #Adds the first letter as capital and the rest into lowercase
"".lower() #Makes all the string lowercase
"".upper() #Makes all the string uppercase


print("kyle".title())
print("KYLE".lower())
print("kyle".upper())


name = input("Name: ").lower()

if name == "kyle":
    print("this works")
else:
    print("this is wrong.")


example_string = "hello hello world"

print(example_string.count("hello")) # -> 2 instance of hello in this string

print(example_string.replace("world", "WORLD"))

print(len(example_string)) # -> number of characters in string


# isalpha Method - checks if the entire string is only the letters a-z no special case letters

example_isalpha_string = "Hello"

print(example_isalpha_string.isalpha()) #-> true


# isalnum Method - checks if the string is alphanumeric - letters a-z OR numbers 0-9 OR BOTH

print(example_isalpha_string.isalnum()) #-> true

example_isalnum_string = "Hello 12"

print(example_isalnum_string.isalnum()) #-> false

# Special Characters Including spaces are NOT alphanumeric so the value returned is false