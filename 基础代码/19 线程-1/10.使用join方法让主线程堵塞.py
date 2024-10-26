# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 21:34
# @Author  : 顾安
# @File    : 10.使用join方法让主线程堵塞


"""
子线程执行任务时可以让主线程堵塞
"""

import threading
import time


def work():
    for i in range(1, 6):
        print(i)
        time.sleep(1)


t1 = threading.Thread(target=work)
t1.start()
t1.join()  # 当子线程任务执行完毕之后才能继续执行主程序没有执行完的代码

print('这是主线程打印的信息...')
