'''
Arrays/Lists

An array is a list of things specifically different datatypes
'''

example_array = ["String",1,True,2.2]

for i in example_array:
    print(type(i))

#This will show the datatype of each item in the example_array



import random

example_array_two = ["hi", "bye", "sigh"]

#An array has indexes which are the way you reference the individual values inside of them

print(example_array_two[0]) #-> "hi"
print(example_array_two[1]) #-> "bye"
print(example_array_two[2]) #-> "sigh"

#print(example_array_two[3]) #-> Would produce an error because there is no 4th item in the list

#METHODS FOR ARRAYS

item = "exampleItem"
index =  random.randint(1,len(example_array_two))

print("--Array Append Example--")
example_array_two.append(item) #-> adds whatever is inside the brackets onto the end of the example_array_two
print(example_array_two)

print("--Array Insert Example--")
example_array_two.insert(index, "Inserted Array") #-> adds whatever is inside the brackets into a specific index of the example_array_two
print(example_array_two)

print("--Array Reverse Example--")
print(example_array_two)
example_array_two.reverse() #-> reverses the array

print("Up: Unreversed Array \nBelow: Reversed Array")
print(example_array_two)