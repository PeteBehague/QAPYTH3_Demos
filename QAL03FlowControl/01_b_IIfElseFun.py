


mark = int(input("Enter mark: "))
if mark > 65:
    print("Pass")

mark = int(input("Enter another mark (greater than 65 for a pass): "))
if mark > 65:
    print("Pass")
else:
    print("Fail")

mark = int(input("Enter mark (> 75 for a merit and > 65 for a pass): "))
if mark > 75:
    print("Merit")
elif mark > 65:
    print("Pass")
else:
    print("Fail")

mark = int(input("Enter mark (> 85 for a distinction, > 75 for a merit and > 65 for a pass):  "))
if mark > 85:
    print("Distinction")
elif mark > 75:
    print("Merit")
elif mark > 65:
    print("Pass")
else:
    print("Fail")

# Menu
print("Menu:")
print("1 - Add")
print("2 - Amend")
print("3 - Delete")
print("4 - Display")
menu_option = int(input("Enter Option: "))
if menu_option == 1:
    print("Option 1 - Add selected")
elif menu_option == 2:
    print("Option 2 - Amend selected")
elif menu_option == 3:
    print("Option 3 - Delete selected")
elif menu_option == 4:
    print("Option 4 - Display selected")
else:
    print("Invalid option selected")


# Nested If's
print("Menu:")
print("3 - Level 3")
print("4 - Level 4")

examlevel = int(input("Enter exam level: "))

if examlevel == 3:
    mark = int(input("Enter level 3 mark: "))
    if mark > 65:
        print("Pass")
    else:
        print("Fail")
elif examlevel == 4:
    mark = int(input("Enter level 4 mark: "))
    if mark > 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Level")

# If with multiple conditions
print("Menu:")
print("1 - Level 1")
print("2 - Level 2")
print("3 - Level 3")
print("4 - Level 4")
examlevel = int(input("Enter exam level: "))
if examlevel == 1 or examlevel == 2:
    mark = int(input("Enter Level 1 or 2 mark: "))
    if mark > 75:
        print("Pass")
    else:
        print("Fail")
elif examlevel == 3 or examlevel == 4:
    mark = int(input("Enter Level 3 or 4 mark: "))
    if examlevel == 3 and mark > 65:
        print("Pass")
    elif examlevel == 4 and mark > 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Level")

word = input("Enter a word")
