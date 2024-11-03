# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 21:37
# @Author  : 顾安
# @File    : 3.使用生成器完成任务切换.py

import time


def work_1():
    for i in range(10):
        print('work_1', i)
        time.sleep(0.1)
        yield


def work_2(obj):
    for _ in range(5):
        print('work_2被执行')
        next(obj)
        time.sleep(0.1)


gen_obj = work_1()
work_2(gen_obj)
