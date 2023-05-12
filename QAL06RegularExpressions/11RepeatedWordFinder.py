import re

text = 'bug bug and fou fou were going to the the fair to win some win some coconuts nuts'
pattern = r'\b(\w+)\b\s+\1\b'

print(re.sub(pattern, r'\1', text))
