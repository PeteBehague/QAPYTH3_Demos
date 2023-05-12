import re

# Examples taken from https://www.w3schools.com/python/python_regex.asp

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

# Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

x = re.findall("ai", txt)
print(x)

x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())

# The Match object
x = re.search("ai", txt)
print(x)  # this will print an object

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

x = re.search(r"\bS\w+", txt)  # looks for any words that start with an upper case "S"
print(x.span())
print(x.string)
print(x.group())
