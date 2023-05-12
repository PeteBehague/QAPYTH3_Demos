def change_list(inlist, inlist_as_slice, val, times):
    inlist += str(val) * times
    inlist_as_slice += str(val) * times
    val = 'oh!'
    times = 10

mylist=[]
myslice = mylist.copy()
mystring = 'h'
mynumber = 8
change_list(mylist, myslice[:], mystring, mynumber)
print(f"mylist: {mylist}")
print(f"myslice: {myslice}")
print(f"mylist: {mystring}")
print(f"mylist: {mynumber}")
