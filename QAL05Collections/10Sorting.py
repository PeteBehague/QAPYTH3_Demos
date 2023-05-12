cheese = ['Cornish Yarg', 'Oke', 'Edam', 'Stilton']
cheese.sort(key=len)
print(cheese)

nums = ['1001', '34', '3', '77', '42', '9', '87']
#       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Note the numbers are strings 
newstr = sorted(nums)
newnum = sorted(nums, key=int)
print(f"newstr: {newstr}")
print(f"newnum: {newnum}")

