import re

# Class Shortcuts
word = "abc9 3Z"
m = re.search(r'^abc\d\s\d\w$', word)
print(m)


name = "Johnathon Johnson JOHNson"
m = re.search(r'(?im)^john', name)
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())

m = re.search(r'^john', name, re.IGNORECASE|re.MULTILINE)
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())

m = re.search(r'^(?i:j)ohn', name) # case insensitive match but for just the letter "j". The following "ohn" must be lowercase
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())
