print("\nRun for 10 iterations")
count = 0
for i in range(10):
    count = count + 1
    print("i:", i, "count", count)

print("\nFrom 5 to 9")
for i in range(5, 10):
    print("i:", i)

print("\nSteps of 2")
for i in range(10, 20, 2):
    print("i:", i)

print("\nLoops inside loops")
for i in range(3):
    for j in range(4):
        print(i, "*", j, "=", i*j)
