mytuple = 'eggs', 'bacon', 'spam', 'tea'

# Value error: too many values to unpack
# x, y, z = mytuple

# we can designate any variable on the left as a tuple by prefixing with an asterisk *
x, y, *z = mytuple
# tuple2 = mytuple
print(x, x, z)


t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
t2 = 'kelp', 'crab', 'lobster', 'fish'
for a, *b, c in t1, t2:
    print(a, b, c)
