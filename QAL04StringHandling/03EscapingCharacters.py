# \r - carriage return
# \n - linefeed

print(  '\r\n \1\2\3') # \1\2\3 may print as a sequence of special characters or as is done here a set of "not printable" chars

# the r before the string indicates to treat the string as a raw string (treat all '\' chars as their literal values
print( r'\r\n \1\2\3')
