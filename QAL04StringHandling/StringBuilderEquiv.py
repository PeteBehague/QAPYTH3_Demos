from io import StringIO

a = ['Hi ', 'this ', 'is ', 'Python']
string = StringIO()
for i in a:
    string.write(i)
print(string.getvalue())


class StringBuilder:
    string = None

    def __init__(self):
        self.string = StringIO()

    def append(self, str):
        self.string.write(str)

    def __str__(self):
        return self.string.getvalue()


a = "Banana"
string_builder = StringBuilder()
string_builder.append("Welcome ")
string_builder.append("Mr/Ms/Mrs.")
string_builder.append(a)
print(string_builder)


mylist = ['abcd' for i in range(5)]
mystring = "".join(mylist)
print(mystring)
