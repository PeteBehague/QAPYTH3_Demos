import sys

for idx, arg in enumerate(sys.argv):
    print('index:', idx, 'argument:', arg)

# Launch from terminal:
# python 10enumerate.py apple pear orange banana

print("\nFor each line in a file")
for nr, line in enumerate(open('brian.txt'), start=1):
    print(nr, line, end="")
