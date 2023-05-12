# Strings
my_strings = 'Norwegian Blue', "Mr. Khan's bike"
print(my_strings)
print(my_strings[1])

# Lists
cheeses = ['Cheddar', ['Camembert', 'Brie'], 'Stilton']
print(cheeses)
print(cheeses[0])
print(cheeses[1])
print(cheeses[1][1])
cheeses[2] = "Stinking Bishop"
print(cheeses)

# Tuples
random_stuff = (47, 'Spam', 'Major', 683, 'Ovine Aviation', 683)
#                                                           ^^^ duplicate
print(random_stuff)
print(random_stuff[2])
# tuples are immutable
# random_stuff[2] = "colonel"

# Sets
set_of_random_stuff = {47, 'Spam', 'Major', 683, 'Ovine Aviation', 683}
#                                                                  ^^^ duplicate
print(set_of_random_stuff)
# set_of_random_stuff[2] = "colonel"

# Dictionaries
jobs = {'Totnes': 'Barber', 'BritishColumbia': 'Lumberjack'}
print(jobs)
print(jobs['BritishColumbia'])
jobs['BritishColumbia'] = 'Ski Instructor'
print(jobs['BritishColumbia'])

