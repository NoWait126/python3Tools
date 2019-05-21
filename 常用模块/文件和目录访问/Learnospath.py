# -*- coding: utf-8 -*-

import os
'''
该模块支持python2和python3，不过
有些方法是对os.path的封装，比os.path更加简便
提供的Purepath其语义适用于不同的操作系统，可以让代码仅操作路径而不实际访问操作系统，对跨平台访问很有用。
'''

def testFunc():
    print("p 路径为 'D:/codes/PythonTools/README.md'")
    p = 'D:/codes/PythonTools/README.md'
    print("abspath(p):获取绝对路径", os.path.abspath(p))
    print("split(p):返回目录和文件名称二元组", os.path.split(p))
    print("exists(p):判断路径是否存在", os.path.exists(p))
    print("获取父级目录",os.path.dirname(os.getcwd()))
if __name__ == '__main__':
    testFunc()