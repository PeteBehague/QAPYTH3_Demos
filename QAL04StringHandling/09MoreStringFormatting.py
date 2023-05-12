print("\nFloat")
flt = 22/7
print("Float: {0:11.8f}, sci: {0:e}".format(flt))

print("\nText")
first = 'Gengis'
second = 'Khan'
print("Name: {:<20s} {:<10s}".format(first, second))

print("\Planets")
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

for i, key in enumerate(planets.keys(), 1):
    # option 1
    print("{:2d} {:<10s} {:06.2f} Gm".
          format(i, key, planets[key]))

    # option 2 - interpolation
    print(f"{i:2d} {key:<10s} {planets[key]:06.2f} Gm")

# {2d}	 Right-justified, at least two digits, space padding
# {<10s} Left-justified, at least 10 character string, space padding
# 06.2f} Right-justified, at least 6 characters, zero padding. One of the six characters is the decimal point,
#        and the argument is rounded to two digits after the decimal point


