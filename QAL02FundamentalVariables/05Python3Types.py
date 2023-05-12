# Numbers
a = 3.142
b = 42
c = 0x3f
# Bytes
ab = b'Norwegian Blue'
ac = b"Mr. Khan's bike"
#strings
sb = 'Norwegian Blue'
sc = "Mr. Khan's bike"
# tuples - note use of round bracket. Tuples are immutable
tup = (47, 'Spam', 'Major', 683, 'Ovine Aviation')
# Lists - note use of square brackets. Lists are mutable
lst = ['Cheddar', ['Camembert', 'Brie'], 'Stilton'] # contains list in a list!
# Bytearrays - note use of keyword - bytebrrays are mutable
byte_ary = bytearray(b'abc')
# Dictionaries - note use of curly brackets and colons. Dictionaries are mutable
dic = {'Sword': 'Excalibur', 'Bird': 'Unladen Swallow'}
# Sets - note use of curly brackets. Sets are mutable
a_set = {'Chapman', 'Cleese', 'Idle', 'Jones', 'Palin'}
a_set.discard('Cleese')
a_set.add('Fawltey')
print(a_set)
a_set.add('Fawltey')
print(a_set)

# Booleans
number1 = float(input("Please enter first number : "))
number2 = float(input("Please enter second number: "))
if number1 > number2:
    number1bigger = True
else:
    number1bigger = False

print("number1 bigger:", number1bigger)

if number1bigger:
    print("number1 bigger")
else:
    print("number1 not bigger")



