import re

line = 'words*separated*by*asterisks'
elems = re.split('[*]', line)
print(elems)

line = 'root:;0.0:superuser,/root;/bin/sh'
elems = re.split('[:;.,]', line)
print(elems)
