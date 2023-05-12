import os

path = '.'

def scan_folder(path, indent_size):
    for entry in os.scandir(path):
       stat = entry.stat()
       if entry.is_file():
           # print("%-16s %d" % (entry.name, stat.st_size))
           spaces = '\t'*(indent_size)
           print(f"{spaces}{entry.name} {stat.st_size}")
       elif entry.is_dir():
           spaces = '\t' * (indent_size)
           print(f"{spaces}DIRECTORY: {entry.name}")
           path + rf"\{entry.name}"
           scan_folder(path + rf"\{entry.name}", indent_size + 1) # recursive call



scan_folder(path, 0)