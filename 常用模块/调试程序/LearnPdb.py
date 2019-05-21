# -*- coding: utf-8 -*-

import pdb

'''
程序调试一般的方式有print、assert、logging、pdb

print使用完要删除不方便

assert本身也可能会发生异常

logging是不错的，可以自定义级别，debug，info，warning，error

pdb 可以让程序以单步方式运行，可以随时查看运行状态，类似于C语音的gdb

下面的程序可以使用 python -m gdb LearnPdb.py执行

执行后输入 n表示下一步； l表示显示代码； p n表示打印变量n
'''

def mod(a, b):
    a = a + 1
    b = b -2
    return a / b
if __name__ == '__main__':
    mod(1, 2)