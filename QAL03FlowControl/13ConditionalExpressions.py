i = 42
j = 3

if i > j:
    print("i gt j")
else:
    print("i lt j")

print("i gt j") if i > j else print("i lt j")

print("i gt j" if i > j else "i lt j")


a = 4
b = 5
print(-1 if a < b else (+1 if a > b else 0))

print("\nBewareOfPrecedence")
for a in [54, 34, 42]:
    print("a = ", a)
    answer = a + 5 if a < 42 else 0
    print(answer)
    answer = a + (5 if a < 42 else 0)
    print(answer)
