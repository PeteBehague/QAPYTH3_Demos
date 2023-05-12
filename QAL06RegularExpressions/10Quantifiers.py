import re

# Date matcher. How rigorous is this?
value = '30/12/2021'

m = re.search(r'^([0][1-9]|[1-2][0-9]|(3)[0-1])(\/)(((0)[1-9])|((1)[0-2]))(\/)\d{4}$'
              , value)
if m:
    print('The value is valid!')


