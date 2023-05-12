myn = [45, 66, 12,  99, 3.142, 42]
print("length: ", len(myn))
print("min:", min(myn), "max:", max(myn))
print("sum:", sum(myn))

myd = {'fred':3, 'jim':8, 'dave':42}
print("min:", min(myd), "max:", max(myd))
print("length: ", len(myd))

# The len function returns the number of characters when used with a string,
# and the number of bytes when used with a bytes object.
mys = chr(0x20ac)
print(mys, len(mys))
myb = mys.encode()
print(myb, len(myb))
