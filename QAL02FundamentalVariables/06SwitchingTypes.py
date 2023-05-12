from decimal import Decimal

num = 42
pi  = 3.142
num = 42/pi
print(num)

count = 45
# TypeError: Can't convert 'int' object to str implicitly
# print("Unused port: " + count)

# Fix
print("Unused port: " + str(count))

# float to integer
print("float to int")
number = 2.6
integer1 = number
integer2 = round(number)
integer3 = int(round(number))
print(number)
print(integer1)
print(integer2)
print(integer3)

# integer to float
print("int to float")
number = 2
flt = float(number)
print(number)
print(flt)

# casting
print("casting")
integer1 = int(10.0)
integer2 = int(3.5)
answer = integer1 / integer2
print(answer)
answer = float(integer1) / integer2
print(answer)
answer = float(integer1) / float(integer2)
print(answer)

# casting decimals
print("casting decimals")
number1 = 1
number2 = 7
print(type(number1))
print(number1 / number2)
number1 = Decimal(1)
number2 = Decimal(7)
print(type(number1))
print(number1 / number2)



