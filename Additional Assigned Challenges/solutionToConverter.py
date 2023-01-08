ml_or_l = input("Would you like to convert \nml to l \nor \nl to ml: ")
value = float(input("What value do you want to convert: "))

if ml_or_l == "ml to l":
    print(f"converted value: {value / 1000}")
elif ml_or_l == "l to ml":
    print(f"converted value: {value * 1000}")
else:
    print("Invalid Value")

# try it if you don't understand
# keep trying until you figure out how the code works
