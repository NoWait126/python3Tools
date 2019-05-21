# -*- coding: utf-8 -*-

'''
lambda匿名函数

当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]
等同于
def f(x):
    return x * x

'''

def testLambda():
    l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(l)

if __name__ == "__main__":
   testLambda()