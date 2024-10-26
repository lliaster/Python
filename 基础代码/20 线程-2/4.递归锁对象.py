# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 20:54
# @Author  : 顾安
# @File    : 4.递归锁对象


import threading

num = 0
# lock_obj = threading.Lock()  # 互斥锁对象
lock_obj = threading.RLock()  # 递归锁对象


def add():
    global num
    for i in range(1000000):
        lock_obj.acquire()
        lock_obj.acquire()
        num += i
        lock_obj.release()
        lock_obj.release()


def sub():
    global num
    for i in range(1000000):
        lock_obj.acquire()
        lock_obj.acquire()
        num -= i
        lock_obj.release()
        lock_obj.release()


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()

print('主线程打印的全局变量的结果:', num)

"""
避免死锁的方案:
    1.线程锁建议全局只有一个
    2.尽量使用递归锁
"""
