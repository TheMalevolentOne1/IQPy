'''
Write a program that:
• converts and outputs marks into
grades, using the following data:
Greater than or equal to 75
A
Greater than or equal to 60
B
Greater than or equal to 35
C
Less than 35
D

Variables
If/Elif/Else #please see first if statement
'''
mark = int(input("Mark: "))
if mark >= 75:
    print("Grade A")
elif mark >= 60:
    print("Grade B")
elif mark >= 35:
    print("Grade C")
elif mark < 35:
    print("Grade D")
# uses if and elif to compare mark to find the mark