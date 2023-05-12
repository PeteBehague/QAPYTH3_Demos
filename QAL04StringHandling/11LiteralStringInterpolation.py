names = ['Tom', 'Harry', 'Jane', 'Mary']
s = f"The third member is {names[3]}"

print(s)

planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

for i, key in enumerate(planets.keys(), 1):
    # option 2 - interpolation
    print(f"{i:2d} {key:<10s} {planets[key]:06.2f} Gm")



