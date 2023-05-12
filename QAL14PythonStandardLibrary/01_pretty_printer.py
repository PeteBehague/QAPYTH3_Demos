import pprint

myd = {'UK':['London', ('Wigan', 'Macclesfield', 'Bolton')],
       'US':['Washington', ('Springfield', 'New York', 'Boston')],
       'FR':['Paris', ('Lyon', 'Bordeaux', 'Toulouse')]
}

print("Standard Print: ")
print(myd)

print("\nPretty Print: ")
pprint.pprint(myd)
