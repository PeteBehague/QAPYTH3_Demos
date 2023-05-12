from ctypes import *
from ctypes.wintypes import *

class STARTUPINFO(Structure):
    _fields_ = [
        ("cb",              DWORD),
        ("lpReserved",      LPSTR),
        ("lpDesktop",       LPSTR),
        ("lpTitle",         LPSTR),
        ("dwX",             DWORD),
        ("dwY",             DWORD),
        ("dwXSize",         DWORD),
        ("dwYSize",         DWORD),
        ("dwXCountChars",   DWORD),
        ("dwYCountChars",   DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags",         DWORD),
        ("wShowWindow",     WORD),
        ("cbReserved2",     WORD),
        ("lpReserved2",     c_char_p), #LPBYTE
        ("hStdInput",       HANDLE),
        ("hStdOutput",      HANDLE),
        ("hStdError",       HANDLE)
    ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD)
    ]


kernel = windll.kernel32

Startup = STARTUPINFO(0)
ProcInfo = PROCESS_INFORMATION(0)

retn = kernel.CreateProcessA(None, br"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.exe",
                             None, None,
                             False, 0, None, None,
                             byref(Startup),
                             byref(ProcInfo))

print(WinError())
