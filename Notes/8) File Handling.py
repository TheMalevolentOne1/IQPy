'''
Text File Handing

w = write to a file (This will override everything that exists)
a = append this will add to the file
r = read this will read the contents of the file
x = creates a new file


'''

import os

try: # ignore
    open("newTextFile", 'x')

    file = open("newTextFile", 'a')

    file.write("This text will be added to the new file")

    file.close()


except FileExistsError: # ignore
    arr = os.path.abspath(__file__).split("\\")
    arr.pop()
    print(arr)
    arr = "/".join(arr)
    os.remove(arr+"/newTextFile.txt")
