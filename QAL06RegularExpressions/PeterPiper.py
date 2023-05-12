import re

str = "Peter Piper picked a peck of pickled peppers. " \
      "A peck of pickled peppers Peter Piper picked. " \
      "If Peter Piper picked a peck of pickled peppers, " \
      "Where’s the peck of pickled peppers Peter Piper picked?"

Myvar = re.findall("p[aeiou]ck", str)

print(Myvar)