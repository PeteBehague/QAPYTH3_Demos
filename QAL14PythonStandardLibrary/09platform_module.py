import sys
import platform

print(sys.platform)
print("Platform:", platform.platform())
print("Compiler:", platform.python_compiler())
print("Python  :", platform.python_version())
print("LibC :", platform.libc_ver()) # unix only
