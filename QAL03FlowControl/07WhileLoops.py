line = None

while line != 'done':
    line = input('Type "done" to complete: ')
    print('<', line, '>')


myl = [23, 67, 32, 9, 77]
while myl:
    print(myl.pop() * 2)

print(myl)  # Note what myl contains after the loop ends

