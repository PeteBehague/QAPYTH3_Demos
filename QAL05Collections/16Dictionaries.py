mydict = {'Australia':'Canberra', 'Eire':'Dublin',
          'France':'Paris', 'Finland':'Helsinki',
          'UK':'London', 'US':'Washington'
}
print(mydict['UK'])

country = 'Iceland'
mydict[country] = 'Reykjavik'

print(mydict)

mylist = ('Bill', 'Ted', 'Anthia')
mydict = {}.fromkeys(mylist)
print(mydict)
keys = list(mydict)
print(keys)
