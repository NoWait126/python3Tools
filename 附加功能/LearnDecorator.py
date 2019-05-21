# -*- coding: utf-8 -*-

import time

'''
装饰器

由于函数也是一个对象，而且函数对象可以被赋值给变量，即函数也可以作为一个参数，这种方法可以增强函数的功能同时不会改变函数原有的方法

本质上，decorator就是一个返回函数的高阶函数，使用装饰器的时候就是把被使用函数前一行加上 `@装饰器名称`

PS：编写Python类的时候，有时候会遇到类里面的函数上有`@classmethod`，这就是使用了装饰器，表示该函数是一个类内函数，可以由类直接调用，而非类内函数则是由实例调用的

'''


# 一个简单装饰器的例子，想要在计算的同时获取一下当前的时间，但是又没有改变计算函数的原有功能
def addPrintData(func):
    def printData(*args, **kw):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return func(*args, **kw)
    return printData

@addPrintData
def simpleDecorator(a, b):
    print("The sum of args is %d" % (a + b))



if __name__ == '__main__':
    simpleDecorator(2, 3)
