# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 21:49
# @Author  : 顾安
# @File    : 2.多任务并行执行.py


"""
并发: 在同一时刻, 只有部分任务被执行, 没有被执行的任务等待系统轮询调度
并行: 在同一时刻, 多个任务同时执行
"""

import multiprocessing
import time


def work_1(name):
    for i in range(1, 6):
        print(f'{name}被执行了: {i}')
        time.sleep(1)


def work_2(name):
    for i in range(1, 6):
        print(f'{name}被执行了: {i}')
        time.sleep(1)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work_1, args=('安娜',))
    p2 = multiprocessing.Process(target=work_2, args=('双双',))

    p1.start()
    p2.start()

    p1.join()  # 让主进程堵塞
    p2.join()
    print('主进程打印的信息...')
