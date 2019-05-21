# -*- coding: utf-8 -*-

import queue, threading, time

'''
queue 模块实现多生产者，多消费者队列。当信息必须安全的在多线程之间交换时，它在线程编程中是特别有用的

它包含三种队列：Queue、LifoQueue、PriorityQueue

本测试用例是有两个线程，一个是生成者另外一个是消费者，生产者将任务放到队列中，消费者去执行任务

'''

task = queue.Queue(5)
lock = threading.Lock()
stopFlag = False

def doTask(task):
    while not stopFlag:
        lock.acquire()
        if not task.empty():
            try:
                t = task.get()
            finally:
                lock.release()
            print("do task %s" % t)
        else:
            break

def createTask(task):
    todoList = ["read book", "codes", "write paper"]
    for i in todoList:
        lock.acquire()
        if task.full():
            lock.release()
            time.sleep(0.5)
        else:
            try:
                task.put(i)
            finally:
                lock.release()
            print("put task %s" % i)

producer = threading.Thread(target=createTask, args=(task,), name='produer')
consumer = threading.Thread(target=doTask, args=(task,), name='consumer')
producer.start()
consumer.start()
producer.join()
consumer.join()

while not task.empty():
    pass

stopFlag = True

print("work finish")