mytuple=('eggs', 'bacon', 'spam', 'tea', 'beans')
print(mytuple[2:-1])

print(mytuple[-4])

mylist = list(mytuple)
print(mylist[1:])

print(mylist[:2])

print("\nremoving items")
# List elements may be removed using del
cheese = ['Cheddar', 'Camembert', 'Brie', 'Stilton']
del cheese[1:3]
print(cheese)
