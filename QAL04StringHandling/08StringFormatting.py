var1 = 42
var2 = 'hello'
print("{name} {value}".format(value=var1, name=var2))


var1 = 234.123456
var2 = 234
var3 = 234.123456

s = "var1: {0:>+15.3f} var2: {1:<-8d} var3:{2:10.2f} the end".format(var1, var2, var3)

print(s)
