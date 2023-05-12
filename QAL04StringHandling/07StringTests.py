import re

name = "Fred Quimby"
substr = input("What are you looking for? ")
if substr in name:
    print(f"{name} does contain {substr}")


text = 'hello world'

print(text.count('o'))

if text.startswith('hell'):
    print("It's hell in there")

if text.isalpha():
    print('string is all alpha')

text = ' \t\r\n'
if text.isspace():
    print('string is whitespace')

print("\nUsing regular expressions")
text = 'hello world'
print(len(re.findall(r"(o)", text)))
print(len(re.findall(r"(o)", text[5:])))

if re.match(r"^hell", text):
    print("It's hell in there")

    if re.match(r"^[A-Za-z]+$", text):
        print("string is all alpha")

    text = ' \t\r\n'
    if re.match(r"^\s+$", text):
        print("text is whitespace")