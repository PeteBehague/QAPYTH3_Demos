import subprocess
# setting stdout and stderr to use subprocess.PIPE means that tasklists'
# output will be returned to the parent rather than being directly printed.
proc = subprocess.run("tasklist",
	stdout=subprocess.PIPE,
	stderr=subprocess.PIPE)

if proc.stderr != None:
    print ("error:", proc.stderr.decode())

print("output:", proc.stdout.decode())
