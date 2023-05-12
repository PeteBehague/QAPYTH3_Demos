# Program : 06MoreTricks
# Purpose : Demonstrates print doesn't have to write to stdout

import sys

output = open('06MoreTricks.dat', 'w')
print("Hello", file=output)
print("Oops, we had an error", file=sys.stderr)

# file writing is usually buffered
output.flush()
print("Everyone", file=output)

# Closing file will also flush the stream
output.close()

pass