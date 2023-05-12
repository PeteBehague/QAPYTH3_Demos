import sys
import fileinput
import re
import glob

pattern = sys.argv.pop(1)

if len(sys.argv) > 1:
    if sys.platform == "win32":
        sys.argv[1:] = glob.glob(sys.argv[1])

    more_files = len(sys.argv[1:])
else:
    more_files = 0

for line in fileinput.input():
    m = re.search(pattern, line)

    if m:
        if more_files > 1:
            print(fileinput.filename(), ": ", end="")
        print(line, end="")
