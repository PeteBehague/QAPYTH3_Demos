# Program : 05StandardStream
# Purpose : Demonstrates use of the three standard IO streams stdin, stdout and stderr
# and how they can be used like any other file object

import sys
sys.stdout.write("Please enter a value: ")
sys.stdout.flush()
reply = sys.stdin.readline()
# reply = sys.stdin.readline().rstrip()  # strip off newline char

print("<", reply, "> was input")
