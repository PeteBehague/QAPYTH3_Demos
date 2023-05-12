import re

line = "Some punctuation, is present. As is some repeating whitespace  \n  and some text."
sound = "bonnk went the hammer as it hit the anvil, boinkk, boinkkk, boinkboink, boinkboinkboink. There it goes again."

m = re.search(r'[:;,]?\s*\w+', line)
print(m)

m = re.search(r'boink+', sound)
print(m)

m = re.search(r'(boink)+', sound)
print(m)

