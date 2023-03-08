'''
Challenge 23
A gardener needs to buy some turf for a project
they are working on. The garden is rectangular
with a circular flower bed in the middle.
Write a program that:
• asks the user for the dimensions of the lawn
and the radius of the circle (in metres)
• uses a function to calculate and output
the amount of turf needed
You will need to use:
Variables
If/Elif/Else
Functions

Tip: Circle area = Pi x Radius2

Pi  = 3.14159265359
'''
import math

length = int(input("Please input length of the garden"))
width = int(input("Please input width of the garden"))
rad = int(input("Please input radius of the flowerbed in metres"))
area_gar = length * width


def circle_area(rad):
    return math.pi * (rad ** 2)


print(f"The Area of your garden is {length * width} m^2")
print(f"The Area of the flower bed is {round((circle_area(rad)))}")
print(f"The Amount of Turf needed is {round(area_gar - circle_area(rad))}")
