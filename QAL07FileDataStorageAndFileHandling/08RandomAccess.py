fh = open('08country.txt', 'rb') # Need to create country.txt file

index={}
while True:
    line = fh.readline()
    if not line: break
    fields = line.decode().split(',')
    index[fields[0]] = fh.tell() - len(line)

key = input('Enter a country:')
fh.seek(index[key])
print(fh.readline().decode(), end="")
