import re
string = 'Red and yellow and pink and green, purple and orange and blue I can sing a rainbow'
result = re.sub('[Rr]ed|yellow|pink|green|purple|orange|blue', 'black', string)
print(result)

string = 'Red and yellow and pink and green, purple and orange and blue I can sing a rainbow'
result, num = re.subn('[Rr]ed|yellow|pink|green|purple|orange|blue', 'grey', string)
print(f"{result}\nThere were {num} substitutions made")
