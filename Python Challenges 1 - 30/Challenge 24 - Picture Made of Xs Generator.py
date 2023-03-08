'''
Challenge 24
Write a function that takes two numbers.
The first number indicates the number of
spaces that should be displayed and the
second indicates the number of Xs that
should be displayed. These should both
be displayed on the same line.
Now write another function that makes
multiple calls to your first function and
draws a picture with Xs.

I IS EQUAL TO COUNT VARIABLE

You will need to use:
Variables
Selection
Loops
Functions
'''

def imagecmd(spaces, xs):
    space = ""
    x = ""
    for i in range(spaces):
        space += " "
    for i in range(xs):
        x += "x"
    print(x + space + x + space + x + space + x + space + x)
    print(x + space + space + space + space + space + space + space + x)
    print(x + space + space + space + space + space + space + space + x)
    print(x + space + x + space + x + space + x + space + x)
imagecmd(3, 3)


'''
x0x0x0x0x
x0000000x
x0000000x
x0x0x0x0x

'''