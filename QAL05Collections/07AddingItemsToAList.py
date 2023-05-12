cheese = ['Cheddar', 'Camembert', 'Brie', 'Stilton']

# add to the start of a list
cheese[:0] = ['Cheshire', 'Ilchester']
print(cheese)
# or
cheese.insert(0, "Camenbert")
print(cheese)

# add to the end of a list
cheese += ['Oke', 'Devon Blue']
print(cheese)
# or
cheese.extend(['Gorgonzola', 'Old Crusty'])
print(cheese)
# or
cheese.append(['Lancashire bomb', 'Brie'])
print(cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese.insert(2, 'Cornish Brie')
print(cheese)
# or
cheese[2:2] = ['Cornish Brie']
print(cheese)
