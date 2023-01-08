# While Loops and For Loops

# A while loop is a conditional loop

# while CONDITION:

# The english translation for this is: while (a condition is not met) then

# While Example

user = "" # this defines the user variable as an empty string

'''
while user != "Akos": # while user IS NOT EQUAL to Akos then
    user = input("Name: ").title() # define the user variable as the answer to the question Name:
'''

# For loops are loops that run a certain number of times (they can be used with arrays :) )

# Example For Loop

for i in range(10):
    print("Hello")
    print(i)

# when a for loop is used like above it has something interesting

for i in range(0, 10, 2): # for i in range(start at 0, end at 10, go up by 2) do
    print(i)

# Below make a program that will loop 10 times but only show even numbers starting at 0 - 10
for i in range(0, 12, 2):
    print(i)