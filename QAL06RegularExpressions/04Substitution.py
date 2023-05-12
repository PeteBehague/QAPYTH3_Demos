import re

line = "I'd like a piece of fruit"

cs, num = re.subn('fruit', 'banana', line)
if num:
    print(cs)


line = 'Perl for Perl Programmers'
cs, num = re.subn('Perl', 'Python', line)
if num:
    print(cs)

cs, num = re.subn('Perl', 'Python', line, 1)
if num:
    print(cs)
