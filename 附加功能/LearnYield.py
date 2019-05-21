# -*- coding: utf-8 -*-


'''
首先看下普通的列表生成式
'''

sequence = list(range(1, 11))            # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [x * x for x in range(1, 11)]   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print('list(range(1, 11)):\n',sequence)
print('\n[x * x for x in range(1, 11)]:\n', square)
print('')


'''
为什么有生成器器
 列表生成式可以快速生成列表，可以方便访问数据，但是如果数据量很大的话，比如十万内所有数的平方，那么一次生成这样一个list非常消耗内存，generator可以支持这种一边循环一边计算的机制
 生成器保存的是算法
 
生成器如何创建
 生成器的创建有两种方式
 第一种方式是把list的[]修改为()
 第二种方式是定义的函数中加入yield
   PS：普通函数和有yield的函数的区别
       普通函数是顺序执行，遇到return语句或者函数执行结束即返回，而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
 
生成器如何访问
 生成器的访问用for循环或者next()，生成器也是可以迭代的对象
 
强大的生成器：
  生成器还有更强的的功能，协程就是使用了生成器的原理，实现异步IO操作

'''
# 第一种方法
genSquare = (x * x for x in range(1, 11))
print('类型：', type(genSquare))                    # <class 'generator'>
print(next(genSquare))
for i in genSquare:
    print(i)

# 第二种方法
# 最简单的例子
def simpleGen():
    yield 1
    yield(2)
    yield(3)

simplegen = simpleGen()
print("函数增加了yield关键字：", type(simplegen))     # <class 'generator'>
first = next(simplegen)                           # 1
print("第一次调用获取的值：", first)
second = next(simplegen)                          #2
print("第二次调用获取的值：", second)
third = next(simplegen)                           #3
print("第三次调用获取的值：", third)
