a = 8
b = 9

print(a, b)

# swap references
a, b = b, a

print(a, b)

print("\Cheeses")
# Set values from a numeric range
gouda, edam, caithness = range(3)
print(gouda, edam, caithness)

print("\nrepeated values")
mytuple = 'a', 'b', 'c'
another = mytuple * 4
print(another)

print("\nWatch for single values and the trailing comma")
thing = ('Hello')
print(type(thing))

thing = ('Hello',)
print(type(thing))
