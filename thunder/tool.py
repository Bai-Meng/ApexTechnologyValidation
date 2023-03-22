# --coding: utf-8 --
import win32con
import win32process
from ctypes import *
import win32gui


kernel32 = cdll.LoadLibrary("kernel32.dll")
ReadProcessMemory = kernel32.ReadProcessMemory
WriteProcessMemory = kernel32.WriteProcessMemory
OpenProcess = kernel32.OpenProcess
CloseHandle = kernel32.CloseHandle

# 扫雷游戏窗口
# class_name, title_name = "TMain", "Minesweeper Arbiter "
class_name, title_name = "扫雷", "扫雷"
hwnd = win32gui.FindWindow(class_name, title_name)
hreadID, processID = win32process.GetWindowThreadProcessId(hwnd)
process = OpenProcess(win32con.PROCESS_ALL_ACCESS, 0, processID)

mine_num, w, h, dwSize = c_ulong(), c_ulong(), c_ulong(), c_ulong()
baseAddr = 0x01005330
ReadProcessMemory(process, baseAddr, byref(mine_num), 4, byref(dwSize))
ReadProcessMemory(process, baseAddr+0x4, byref(w), 4, byref(dwSize))
ReadProcessMemory(process, baseAddr+0x8, byref(h), 4, byref(dwSize))
mine_num, w, h = mine_num.value, w.value, h.value
print(f"宽：{w}，高：{h}，剩余雷数：{mine_num}")

max_w, max_h = 30, 24
# 外围有一个值为 0x10 的边界，所以长宽均+2
board_type = (c_uint8 * (max_w + 2)) * (max_h + 2)
board = board_type()
dwBaseAddr = baseAddr+0x10
ReadProcessMemory(process, dwBaseAddr, byref(board),
                  sizeof(board), byref(dwSize))

for y in range(1, h+1):
    for x in range(1, w+1):
        print(hex(board[y][x])[2:].zfill(2), end=",")
    print("\b")



bClear = c_byte(0x8E)
for y in range(1, h+1):
    for x in range(1, w+1):
        if board[y][x] != 0x8f:
            continue
        addr = dwBaseAddr+y*(max_w+2)+x
        WriteProcessMemory(process, addr, byref(bClear),
                           sizeof(c_byte), byref(dwSize))




rect = win32gui.GetClientRect(hwnd)
win32gui.InvalidateRect(hwnd, rect, True)
CloseHandle(process)

