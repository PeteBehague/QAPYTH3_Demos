import sys

num = 42
txt = '3'

try:
    if txt < num:  # syntax error
        print('Wow!')
    else:
        print('Doh!')
except TypeError:
    print("Invalid types compared", file=sys.stderr)
