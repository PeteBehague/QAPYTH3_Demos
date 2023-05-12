import re

line = "eggs<em>I'm saving my strength for running</em><em>I am<\em><em>I am<\em>bacon"

print("\nGreedy Qualifiers")
m = re.search(r'<.+>', line)  # Greedy - '+' means repeated one or more times and looks for as much as possible
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())
    print(m.group())

print("\nLazy Qualifiers")
m = re.search(r'<.+?>', line)  # Lazy - adding the '?' means repeated characters are looked for as little as possible
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())
    print(m.group())

print("\nLazy Qualifiers with additional ?")
m = re.search(r'<.??>', line)  # Lazy - The additional '?' means repeated 0 or 1 time (note in test data there are no
                               # pairs of angle brackets with only one character inside so no matches found - but see
                               # example below)
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())
    print(m.group())
else:
    print("No matches found")

line = "<e>I'm saving my strength for running</e>"
m = re.search(r'<.??>', line)  # Lazy - '?' means repeated 0 or 1 time
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())
