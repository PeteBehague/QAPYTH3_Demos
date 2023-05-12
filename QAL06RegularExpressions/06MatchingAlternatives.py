import re

drink = 'A glass of Coors'
if re.search(r'Bud|Miller|Coors', drink):
    print("It's a beer!")

pattern = r'A (glass|bottle|barrel) of (Bud|Miller|Coors)'

if re.search(pattern, drink):
    print("This drink is suitable for Americans")
