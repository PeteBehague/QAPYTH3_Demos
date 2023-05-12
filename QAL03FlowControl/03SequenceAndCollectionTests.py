mylist = [0, 1, 2, 3]
if mylist:
    print("mylist is True")

my_empty_list = []
if my_empty_list:
    print("my empty list is True") # won't be printed
else:
    print("my empty list is False") # will be printed


# all and any tests
mylist = [0, 1, 2, 3]
# mylist = [-3, 1, 2, 3]
# mylist = [0, 0, 0, 0]

if not all(mylist):  # true if all items in list are true (non-zero items are true)
    print("mylist: not all are True")

if any(mylist):  # true if any single item in the list is true (non-zero items are true)
    print("mylist: at least one item is True")

