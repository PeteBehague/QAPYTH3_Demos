import subprocess
import sys
proc = subprocess.run([sys.executable,'04stuff.py'], input=b"some text")
