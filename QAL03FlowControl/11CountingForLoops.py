some_list = [23, 44, 42, 60, 18, 43, 16]

for i in range(0, len(some_list)):
    if some_list[i] > 42:
        some_list[i] += 1
print(some_list)

print("\nMaintain Own Iterator")
for i in range(0, len(some_list)):
    print(some_list[i])

print("\nUse System Generated Iterator")
for num in some_list:
    print(num)


print("\nIndex needed to alter the sequence")
for idx, num in enumerate(some_list):
    if num > 42:
        some_list[idx] += 1
        some_list.append(some_list[idx] - (42 + 1))  # add more to the collection whilst it's being iterated!
print(some_list)



