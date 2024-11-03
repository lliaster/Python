# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 21:45
# @Author  : 顾安
# @File    : 8.线程池中的future对象.py


"""
线程池中的future对象和asyncio中的future对象没有任何关系
    协程中的future对象是一种可等待的对象, 线程池中的future对象不可等待
"""

import time
from concurrent.futures import ThreadPoolExecutor


def run_func(attr):
    time.sleep(1)
    print('形式参数:', attr)
    return '自定义返回值...'


with ThreadPoolExecutor(max_workers=3) as pool:
    for item in range(1, 6):
        future = pool.submit(run_func, item)
        print('对象信息:', future)
        print('返回值:', future.result())
