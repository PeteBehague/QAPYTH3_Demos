i = 1
j = 120
while i < 42:
    i = i * 2
    if i > j: break
else:
    print("Loop expired: ", i)

print("Final value: ", i)

print("\nSquaring Fun")
count = 0
square = 0
while square < 100:
    count = count + 1
    if count % 2 == 1:  # even numbers only
        continue
    square = count**2
    print(count,"squared =",square)

print("\nIncremental shrinkage")
year = 0
value = 2000
while value > 1000:
    print("year",year,"value",value)
    year = year + 1
    value = value * 0.9
