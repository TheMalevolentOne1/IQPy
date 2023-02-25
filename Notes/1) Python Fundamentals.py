'''
The programming Fundamentals

Sequence - The order in which programs run (line by line)
Selection - If/Elif/Else Statements
Iteration - For/While Loops
'''

#Example of Sequence

print("Hello")
print("World")

#This will print Hello first and World second in order of how they have been written


#Example of Selection

'''
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
'''

import random as rd

x = rd.randint(1,100)

if x < 50:
    print("Less then 50")
elif x > 50 and x <= 99:
    print("Higher then 50")
else:
    print(f"{x} is 100")


#This says if x is less than 50 
#else if x is greater than 50 and less than or equal to 99
#else if both those are wrong then x must be equal to 100


#Example of Iteration

for i in range(5):
    print(i)

# this runs 5 times and prints the counter variable which increases every time it loops
# NOTE THE COUNTER VARIABLE STARTS AT 0

c = 0
while True:
    c+=1
    print(f"while loop {c}")
    if c == 5:
        break

#This is an infinite loop that will run 5 times due to the c variable