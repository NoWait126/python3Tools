# -*- coding: utf-8 -*-

import hashlib


'''
hashlib提供了常见的摘要算法，支持sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s(). md5()

提供一个类似于转换密码的示例，用户输入的密码输入明文，但是输入后保存的时候保存的是加密后的数据
'''

def savaPwd(pwd):
    print("使用md5算法示例：")
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    print(md5.hexdigest())     # hexdigest转出来的是十六进制的串
    print(md5.digest())        # digest转出来的是二进制串

    print("\n使用sha1示例：")
    sha = hashlib.sha1()
    sha.update(pwd.encode('utf-8'))
    print(sha.hexdigest())
    print(sha.digest())

if __name__ == '__main__':
    savaPwd('12345')