# Testing a range of values
number = 4
distance = 25

if 0 < number < 42 < distance:
    print("number and distance are within range")
else:
    print("number and distance are out of range")

# Same as above
if 0 < number and number < 42 and 42 < distance:
    print("number and distance are within range")
else:
    print("number and distance are out of range")

# Can be combined
if 0 < number < 42 and distance != 20:
    print("number is within range and distance is not 20")
else:
    print("either number is not within range or distance is 20 OR number is not within range AND distance is 20")
