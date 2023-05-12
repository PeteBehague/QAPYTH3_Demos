import sys
import time
from datetime import *
from calendar import *

sBirth = input("Enter birthday (dd/mm/yyyy):")
try:
    (day, month, year) = sBirth.split("/")
    dBirth = date(int(year), int(month), int(day))
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    dYesday = date.fromtimestamp(ts - (24 * 60 * 60))

    diff = dYesday - dBirth
    diff = diff.days - leapdays(int(year), dYesday.year)
    years = diff // 365
    print("Client is", years, "years old")
except ValueError:
    print("Invalid date:", sBirth, file=sys.stderr)
    exit(1)


