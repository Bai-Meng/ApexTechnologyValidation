# --coding: utf-8 --

import tkinter
import os

def interface():
    os.system('tool.py')

#变量
win = tkinter.Tk()
#设置窗口
win.title('扫雷外挂')
#设置大小
win.geometry('250x300')

# 定义button
a = tkinter.Button(win,
                   text = '显示地雷位置',  # 按钮的文字
                   bg = 'pink',  # 背景颜色
                   width = 10, height = 1,  # 设置长宽
                   command = interface  # 响应事件：启动外挂
                  )
a.pack()
b = tkinter.Button(win,
                   text = '退出使用外挂',  # 按钮的文字
                   bg = 'pink',  # 背景颜色
                   width = 10, height = 1,  # 设置长宽
                   command = win.quit  # 响应事件：关闭窗口
                   )
b.pack()

#设置窗口图标
#win.iconbitmap('ico/favicon.ico')
#设置背景颜色
win["background"] ="#7AC5CD"#
#设置背景透明度
#win.attributes("-alpha", 0.7)
#显示主窗口
win.mainloop()
