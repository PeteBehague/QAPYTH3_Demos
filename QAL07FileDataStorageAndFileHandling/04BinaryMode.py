# Program : 04BinaryMode
# Purpose : Demonstrates reading and writing to and from binary files

# Unlike most of the other common operating systems, Windows supports text and binary files differently
# With standard text files characters are made up of 2 bytes whereas binary mode writes characters as
# single bytes if a single byte character set (like ISO Latin 1) is being used

fo = open('04lines.txt','wb')
nb = fo.write(b'String made up of single bytes') # nb will contain the number of bytes that were actually written
s = "\r\nNative string as a line\r\n"
nb = fo.write(s.encode())
fo.close()

for line in open('04lines.txt', 'rb'):
    print(line.decode(), end="")
fo.close()













# import base64
#
# message = "Python is fun"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
# new_message_bytes = base64.b64decode(base64_bytes)
# new_message = new_message_bytes.decode('ascii')
#
# print(base64_message)
# print(new_message)
#
# pass
