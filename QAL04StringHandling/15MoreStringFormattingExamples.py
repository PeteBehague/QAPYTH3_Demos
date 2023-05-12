import os
import sys

flt = 22/7
print("Float: {0:11.8f}, sci: {0:e}".format(flt))

first  = 'Gengis'
second = 'Khan'
print("Name: {:<20s} {:<10s}".format(first, second))

# Hexadecimal
usedID = '{:#x}'.format(3735928559)
print(usedID)

file = sys.argv[0]
# The stat module defines constants and functions for interpreting the results of os.stat()
#  st_mode: the most significant (leftmost) two octal digits specify file type,
#  the four least significant are of course the normal file permissions bits.
mode = os.stat(file).st_mode
perms = '0{:o}'.format((mode) & 0o7777) #Octal
print(perms)
