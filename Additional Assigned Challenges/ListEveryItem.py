'''
Use the list provided and use a FOR LOOP to list every individual item in the list as well as its index.
You are not permitted to use notes.

Things needed:
List
For Loop
Variables
'''
list_of_items = ["Chocolate", "Cheat Test Answers", "Hoodies", "Xanax"]

for i in list_of_items:
    print(f"{i} - Index: {list_of_items.index(i)}")

for i in range(len(list_of_items)):
    print(f"{list_of_items[i]} - Index: {i}")

# English: for i in range of the length of list_of_items which would equal 4. print list_of_items and the number
# 1 - 4 due to the length of the list being from 1 to 4. then i would be the values from 1 to 4.
