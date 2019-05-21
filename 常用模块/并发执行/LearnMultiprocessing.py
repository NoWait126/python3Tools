# -*- coding: utf-8 -*-

import os, time, queue
from multiprocessing import Process, Pool


'''
python创建进程有fork()，先了解一下fork()
fork() 作用就是创建一个子进程，该函数比较特殊，一次调用有两个返回值，一个是创建的子进程的id号，一个是父进程的id号

在 multiprocessing 中，通过创建一个 Process 对象然后调用它的 start() 方法来生成进程。 Process 和 threading.Thread API 相同
'''

#一个使用fork的简单例子
def simpleFork():
    print("一个使用fork函数创建进程的简单例子")

    def sayHello(pid):
        print("%d says hello." % pid)

    pid = os.fork()
    if pid == 0:
        sayHello(pid)
    else:
        sayHello(pid)


'''
已经有了fork()可以创建子进程，为什么还要multiprocess？
1 fork()只能在unix环境下使用，无法在Windows环境下使用，而multiprocess是一个可以跨平台运行

2 fork()不会等待子进程或者父进程结束
'''

#一个简单的multiprocess
def simpleMultiprocess():
    print("简单的multiprocess例子")
    def foo(name):
        print("Process %s got %s" % (os.getpid(), name))

    p = Process(target=foo, args=("Process-1",))
    p.start()
    p.join()


'''
Pool类表示工作进程池，支持启动大量的子进程，批量创建子进程
'''
# 使用进程池的简单例子
def printPid(n):
    print("%d is running, index is %d." % (os.getpid(),n))
    time.sleep(5)    # 让每个进程都暂停5s，这样可以更明显的看到几个进程在同时执行

def simplePool():
    print("一个简单使用线程池的例子")
    p = Pool(4)         # 表示同时最多多少个进程在执行
    for i in range(8):  # 创建了8个进程
        p.apply_async(printPid, args=(i,))   # 使用args去调用函数

    p.close()
    p.join()
    print('All subprocesses done.')



if __name__ == '__main__':
    #simpleMultiprocess()  # 思考：尝试将simpleFork()放在前面执行看会出现什么情况！！！
    time.sleep(2)
    print("")

    simplePool()
    time.sleep(2)
    print("")

    simpleFork()
