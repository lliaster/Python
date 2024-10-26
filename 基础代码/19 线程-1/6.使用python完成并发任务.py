# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:48
# @Author  : 顾安
# @File    : 6.使用python完成并发任务

import threading
import time


def work_1():
    for i in range(1, 6):
        print(f'work_1: {i}')
        time.sleep(1)


def work_2():
    for i in range(6, 11):
        print(f'work_2: {i}')
        time.sleep(1)


t1 = threading.Thread(target=work_1)
t2 = threading.Thread(target=work_2)

t1.start()
t2.start()

"""
1.需要通过threading.Thread创建线程对象
2.需要使用target参数绑定线程任务
3.线程对象内部存在启动线程任务的方法: start
"""
