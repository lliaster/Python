# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:43
# @Author  : 顾安
# @File    : 5.使用python完成同步任务


import time


def work_1():
    for i in range(1, 6):
        print(f'work_1: {i}')
        time.sleep(1)


def work_2():
    for i in range(6, 11):
        print(f'work_2: {i}')
        time.sleep(1)


work_1()
work_2()

"""
在以上程序中必须先要等待work_1任务全部完成之后才能执行work_2任务
    像这种类型的结构代码我们称之为单线程同步任务
"""
