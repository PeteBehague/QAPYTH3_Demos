import os
import re
import sys

s = 'Ada Lovelace was the first computer programmer'
result = re.search(r'^\w+', s)
print(result.group())
result2 = re.search(r'\w+$', s)
print(result2.group())

txt = 'Stranger in a strange land'
m = re.search(r'range\b', txt)
print(m.start())

m = re.search(r'range\B', txt)
print(m.start())



# launch code from the terminal using:
# python.exe E:/PycharmProjects/QAL06RegularExpressions/07Anchors.py PythonClub Python C#
name, old, new = ("Python Club", "Club", "Team")
# name, old, new = sys.argv[1:]

new_name = re.sub(fr"{old}$", f"{new}", name)
print(f"Renaming {name} to {new_name}")
#os.rename(name, new_name)