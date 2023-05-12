import re

testy = 'The quick brown fox jumps over the lazy dog'

m = re.search(r"(lazy|fox)", testy)
if m:
    print('Matched', m.groups())
    print('Starting at', m.start())
    print('Ending at', m.end())
