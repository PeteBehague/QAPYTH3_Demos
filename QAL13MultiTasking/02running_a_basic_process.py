import subprocess
import sys

# Run a process and wait for it to complete
# On Windows, no file association is done unless shell=True
proc1 = subprocess.run('hello.py', shell=True)
print('Child 1 exited with', proc1.returncode)

# Don't use a shell if you don't need to:
proc2 = subprocess.run([sys.executable, 'hello.py'])
print('Child 2 exited with', proc2.returncode)
# or the following is analogous:
cmd = sys.executable + ' hello.py '
proc3 = subprocess.run(cmd)
print('Child 3 exited with', proc1.returncode)

proc4 = subprocess.run([sys.executable, '02give_me_data.py', 'Here', 'is', 'some', 'data'])
print('Child 4 exited with', proc4.returncode)



