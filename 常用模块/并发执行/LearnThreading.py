# -*- coding: utf-8 -*-

import threading, time

'''
一 threading库 

Python库提供的基于线程的并行有_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装，一般情况下我们使用threading就够了


二 要点

1 当线程对象一但被创建，调用线程的 start() 方法开始该线程的活动

2 一个线程可以被标记成一个 "守护线程" 。这个标志的意义是，只有守护线程都终结，整个Python程序才会退出  


三 关键函数

1 class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

group：       用于将来扩展

target：      run()方法的可调用对象

name：        线程名称

args：        目标函数参数元祖

kwargs：      目标函数的参数关键字字典

2 start():                    开始线程活动，它在一个线程里最多只能被调用一次，它安排对象的 run() 方法在一个独立的控制进程中调用。

3 run()：                     线程活动的方法

4 join(timeout=None)：        等待，直到线程终结，这会阻塞调用这个方法的线程，直到被调用 join() 的线程终结，里面可以设置超时时间

5 is_alive()：                返回线程是否存活

6 current_thread()：          获取当前的线程名

7 threading.Lock().acquire()  获取锁，只有一个线程可以获取锁，其他的线程会等待释放锁

8 hreading.Lock().release()   释放锁

'''

# 一个简单的线程操作实例
def simpleThread():
    print("一个简单的线程操作")
    def threadsGo():
        print('thread %s is running...' % threading.current_thread().name)
        n = 0
        while n < 2:
            n = n + 1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
            time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)
        print("We set %s sleeping 5s..." % threading.current_thread().name)
        time.sleep(5)

    simplet = threading.Thread(target=threadsGo, name='simplet')
    simplet.start()
    print("We used join(), so only Thread-1 had finish can we go to next step.")
    print("simplet is alive? ", simplet.is_alive())
    simplet.join()
    print("5s is over, we can go to next")


# 线程冲突实例，多个线程修改一个变量
def conflictThread():
    print("一个线程冲突的实例，多个线程修改一个全局变量")
    base = 0
    def addAndSub(n):
        global base
        base = base - n
        base = base + n

    def confictCal(n):
        for i in range(100000):
            addAndSub(n)

    configt1 = threading.Thread(target=confictCal, args=(3,), name='configt1')
    configt2 = threading.Thread(target=confictCal, args=(2,), name='configt2')

    configt1.start()
    configt2.start()

    configt1.join()
    configt2.join()

    print("base result:", base)      # 多次执行可能会出现结果不为0的情况


# 加入锁机制的线程

def addLockThread():
    print("一个线程冲突的实例，多个线程修改一个全局变量")
    base = 0
    lock = threading.Lock()
    def addAndSub(n):
        global base
        base = base - n
        base = base + n

    def confictCal(n):
        for i in range(100000):
            lock.acquire()
            try:
                addAndSub(n)
            finally:
                lock.release()

    configt1 = threading.Thread(target=confictCal, args=(3,), name='configt1')
    configt2 = threading.Thread(target=confictCal, args=(2,), name='configt2')

    configt1.start()
    configt2.start()

    configt1.join()
    configt2.join()

    print("base result:", base)      # 多次执行可能会出现结果不为0的情况


if __name__ == '__main__':
    simpleThread()
    conflictThread()
