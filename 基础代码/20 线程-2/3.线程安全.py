# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 20:32
# @Author  : 顾安
# @File    : 3.线程安全


import threading

num = 0
lock_obj = threading.Lock()  # 线程锁对象


def add():
    global num
    for i in range(1000000):
        lock_obj.acquire()
        num += i
        lock_obj.release()


def sub():
    global num
    for i in range(1000000):
        lock_obj.acquire()
        num -= i
        lock_obj.release()


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()

print('主线程打印的全局变量的结果:', num)

"""
1.多个线程是由操作系统随机调度执行的
2.每个线程执行的任务程序员是无法保证将任务执行完毕之后在完成任务切换的
3.可以使用线程锁来控制线程的随机切换
"""
