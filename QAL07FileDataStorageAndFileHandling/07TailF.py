# Program : 07FTail
# Purpose : Tail F is a unix command which displays lines as they are appended.
# It works by reading to the end-of-file then waiting for one second.
# If a record has been added, then it will be displayed, otherwise we wait for one second again.

import time

fo = open('07TailF.txt','r')
while True:
    line = fo.readline()

    if not line:
        time.sleep(1)
        fo.seek(fo.tell())
        #          ^^^^^^     returns current position of file object (as a number)
        #  ^^^^               places cursor at specified position (in this case the end of the file)
    else:
        print(line, end="")
