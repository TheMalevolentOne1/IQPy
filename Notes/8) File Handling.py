'''
Text File Handing

w = write to a file (This will override everything that exists)
a = append this will add to the file
r = read this will read the contents of the file
x = creates a new file


'''

try: # ignore
    open("newTextFile", 'x')

    file = open("newTextFile", 'a')

    file.write("This text will be added to the new file")
except FileExistsError: # ignore
    print("The file already exists. Ignore this.")
