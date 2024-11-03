# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 20:06
# @Author  : 顾安
# @File    : 2.进程之间不共享资源.py


import time
from multiprocessing import Process

nums = [1, 2]


def work_1():
    for i in range(3, 6):
        nums.append(i)
        time.sleep(1)
    print('进程1执行完毕的最终结果:', nums)


def work_2():
    for i in range(6, 10):
        nums.append(i)
        time.sleep(1)
    print('进程2执行完毕之后的最终结果:', nums)


if __name__ == '__main__':
    p1 = Process(target=work_1)
    p2 = Process(target=work_2)

    p1.start()
    p1.join()

    p2.start()
    p2.join()
    nums = ['a', 'b']
    print('主进程输出的最终结果:', nums)

"""
通过以上输出案例发现每个进程得到的结果不一样
    打印的变量会在各个进程内存中单独存储一份
"""
