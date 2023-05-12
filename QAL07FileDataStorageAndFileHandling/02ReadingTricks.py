# Program : 02 Reading Tricks
# Purpose : Example to demonstrate some of the various forms of reading data from a file

# the read function returns a single long string that contains entire file content
# includes the new line characters
lines = open('01ShakespeareanQuotes.txt').read()

# returns all lines in a List collection.
# The split statement splits on the newline characters and hence they are removed from the individual lines
all_lines_split = open('01ShakespeareanQuotes.txt').read().splitlines()

# the readlines function returns the entire file content but in the form of
# a List (collection) and includes new line chars
linelist = open('01ShakespeareanQuotes.txt').readlines()


# reading a file sequentially in a loop
# Note: "end" strips off new line chars, if we didn't do this printed lines would be double spaced

# inefficient. Reads entire file into memory then iterates through it line by line
for line in open('01ShakespeareanQuotes.txt').readlines():
    print(line,  end="")
#               ^^^^^^ Prevents addition of additional new line character being added to end of line
print("\n")

# efficient. Invoke the file iterator, pulls in one line at a time
for line in open('01ShakespeareanQuotes.txt'):
    print(line, end="")

print("\n")


# safer way to open files - Guarantees closure
with open('01ShakespeareanQuotes.txt', 'r') as infile:
    for line in infile:
        print(line, end='')

# above is analogous to the following:
infile = open('01ShakespeareanQuotes.txt', 'r')
try:
    for line in infile:
        print(line, end='')
finally:
    infile.close()

pass