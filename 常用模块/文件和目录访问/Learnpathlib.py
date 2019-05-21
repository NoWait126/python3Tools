# -*- coding: utf-8 -*-

from pathlib import *
import platform
'''
该模块是python3引入的，提供表示文件系统路径的类，
有些方法是对os.path的封装，比os.path更加简便
提供的Purepath其语义适用于不同的操作系统，可以让代码仅操作路径而不实际访问操作系统，对跨平台访问很有用。
'''

def testFunc():
    print("基础使用，列出子目录、文件等")
    p = Path('.')
    print([x for x in p.iterdir() if x.is_dir()])
    print(list(p.glob('*.py')))
    print("exists()判断路径是否存在",p.exists())
    print("is_dir()判断是否是目录", p.is_dir())
    print("cwd()获取父级目录", Path.cwd())
    print("\n")

    print("纯路径")
    if "Windows" == platform.system():
        q = PureWindowsPath('D:/codes/PythonTools/README.md')
    else:
        q = PureWindowsPath('/home')
    print(q.parents[0])

if __name__ == '__main__':
    testFunc()