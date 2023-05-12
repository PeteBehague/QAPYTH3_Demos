mydict = {}
# del mydict['dob']

if not mydict.pop('dob', False):
    print("Dictionary doesn't contain 'dob' as a key")

