# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 20:02
# @Author  : 顾安
# @File    : 1.内容补充 - 使用上下文管理器的方式管理进程池或线程池对象.py


import time
from concurrent.futures import ThreadPoolExecutor


def work():
    for i in range(1, 11):
        print(i)
        time.sleep(1)


# pool = ThreadPoolExecutor(max_workers=3)
# for _ in range(4):
#     pool.submit(work)
#
# 释放资源
# pool.shutdown()

with ThreadPoolExecutor() as pool:
    for _ in range(4):
        pool.submit(work)
