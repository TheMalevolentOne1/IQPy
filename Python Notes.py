'''
https://mradamscs.files.wordpress.com/2018/06/python_complete.pdf -- link to challenges

The programming Fundamentals

Sequence - The order in which programs run (line by line)
Selection - If/Elif/Else Statements
Iteration - For/While Loops


BASIC DATATYPES

INTEGER - Whole Number
Float - Decimal Number
Bool - Boolean - True or False
String - Quotation Marks

these datatypes can be stored in variables but they are NOT variable names

DATATYPES IN PYTHON
str is short for string
int is short for integer
bool is short for boolean/ true/false
float means decimal numbers

SO I'll show you an example of how to define a type

VARIABLENAME = DATATYPE(input(STRING)) -- this example tells you what to do


Arithmetic Notes

+ means add
- means subtract
* means times
/ means divide
% means modular (don't worry about this piece of shit yet)
** means power (2**2=4)
// means floor division which will divide two numbers and then round to the lowest value as an integer

always include f-string while printing (remember the curly brackets) { }
example:

If/elif/else notes

IMPORTANT SYMBOLS
Symbol | English
!= - not equal to
== - is equal to
<= - greater then or equal to
>= - less than or equal to
> - less than
< - greater then

IMPORTANT KEY WORDS
and
or
not

EXAMPLES OF ABOVE

if 1 == 3:
    print("Hello World")
else:
    print("1 is not equal to 3")

English: if 1 is equal to 1 and 2 is equal to 2 then print Hello World



Libraries

A library is programming made by someone else either built into a programming language
OR made by other developers

Libraries can be:
Time
Random

Or more complex like tkinter which is a GUI creator essentially.


Beginnings of String Manipulation

print("kyle".title())
print("KYLE".lower())
print("kyle".upper())

name = input("Name: ").lower()

if name == "kyle":
    print("this works")
else:
    print("this is wrong.")

Arrays/Lists

An array is a list of things specifically different datatypes

EXAMPLE OF RANDOM

import random

shopping_list = ["orange", "apple", "pear"]

# from here you can use this list of items to get a random choice

print(random.choice(shopping_list))


ARRAY NOTES

example_array = ["hi", "bye", "sigh"]

An array has indexes which are the way you reference the individual values inside of them

EXAMPLE

print(example_array[0]) -> "hi"
print(example_array[1]) -> "bye"
print(example_array[2]) -> "sigh"

print(example_array[3]) -> Would produce an error because there is no 4th item in the list

METHODS FOR ARRAYS

example_array.append(item) -> adds whatever is inside the brackets onto the end of the example_array
example_array.insert(item, index) -> adds whatever is inside the brackets into a specific index of the example_array
example.array.reverse() -> reverses the array
I'll add more when it comes to needing them :)


STRING MANIPULATION

example_string = "hello world"

example_string.count("hello") -> 1
example_string.replace("world", "WORLD") -> print(example_string) -> hello WORLD
len(example_string) -> length of the string -> 11
'''