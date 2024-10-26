# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 21:29
# @Author  : 顾安
# @File    : 9.主线程等待子线程任务完成后才退出

import threading
import time


def work():
    i = 0
    while True:
        print(i)
        i += 1
        time.sleep(1)


t1 = threading.Thread(target=work)
t1.start()

print('这是主线程打印的信息...')

"""
通过以上代码发现主线程必须要等待子线程的任务全部执行完毕之后才能将整个程序退出
"""
