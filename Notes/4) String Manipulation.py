#String Concatenation

x = 100

print("Number: "+x)

#Does not add a space to the end of the string

print("Number:",x)

#Adds a space on the end of the string

print(f"Number: {x}")

#Easiest way to control the formatting of the string


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


example_string = "hello world"

print(example_string.count("hello"))
print(example_string.replace("world", "WORLD"))
print(len(example_string))