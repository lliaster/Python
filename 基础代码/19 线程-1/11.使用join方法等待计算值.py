# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 21:46
# @Author  : 顾安
# @File    : 11.使用join方法等待计算值


import threading

num = 0


def add_():
    # 在一个函数或者一个类的内部使用全局变量(不可变对象)必须用global
    global num
    for i in range(1000000):
        num += i


def sub_():
    global num
    for i in range(1000000):
        num -= i


t1 = threading.Thread(target=add_)
t2 = threading.Thread(target=sub_)
t1.start()
t1.join()  # 主线程等待子线程任务结束时解堵塞

t2.start()
t2.join()

print(num)
