s4 = {23, 42, 66, 123}
s5 = {56, 27, 42}
print("{} {}".format(s4, s5))

s4.remove(123)
s5.add(123)
print("{} {}".format(s4, s5))

s4.pop()
s5.discard(27)
print("{} {}".format(s4, s5))

s5.clear()
print("{} {}".format(s4, s5))

s4 = {23, 42, 66, 123}
s5 = {56, 27, 42}
#update with another's elements
s4 |= s5
print(s4)


s4 = {23, 42, 66, 123}
s5 = {56, 27, 42}
#update with common elements
s4 &= s5
print(s4)


s4 = {23, 42, 66, 123}
s5 = {56, 27, 42}
#remove elements from s4 that can be found in s5
s4 -= s5
print(s4)