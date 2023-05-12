names = ['Tom', 'Harry', 'Jane', 'Mary']
suffix = ['st', 'nd', 'rd', 'th']
n = 1
s = f"{str(n+1) + suffix[n]} of \
{len(names)} is {names[n]}"

print(s)

drive = 'C:'
dir = 'Windows'
path = fr"{drive}\{dir}"

print(path)