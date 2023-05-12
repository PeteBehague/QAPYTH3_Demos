import os

fd = os.open('a_file', os.O_CREAT|os.O_WRONLY, 0o640)
buffer = b'This is some text\r\nanother line\r\n'
bytes = os.write(fd, buffer)
os.close(fd)
print(bytes, 'bytes written')
