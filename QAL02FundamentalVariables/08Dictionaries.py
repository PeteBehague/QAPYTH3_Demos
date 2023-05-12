mydict = {'Australia': 'Canberra', 'Eire': 'Dublin',
          'France': 'Paris', 'Finland': 'Helsinki',
          'UK': 'London', 'US': 'Washington'}

print(mydict['UK'])

country = 'Iceland'
mydict[country] = 'Reykjavik'

print(mydict)

# alternative set up using the dict function
mydict = dict(Sweden='Stockholm',  Norway='Oslo')
print(mydict)

