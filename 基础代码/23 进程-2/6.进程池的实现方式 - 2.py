# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 20:58
# @Author  : 顾安
# @File    : 6.进程池的实现方式 - 2.py


import time
from concurrent.futures import ProcessPoolExecutor, wait  #导入
from multiprocessing import Manager  # 进程池环境中使用的队列

"""
ProcessPoolExecutor: 进程池
ThreadPoolExecutor: 线程池
"""


def write_queue(q):
    for item in [1, 2, 3]:
        q.put(item)
        print('写入的数据为:', item)
        time.sleep(0.5)


def read_queue(q):
    while True:
        item = q.get()
        if item is not None:
            print('读取的数据为:', item)
        else:
            break


def main():
    print('主程序启动...')
    with Manager() as manager:
        queue = manager.Queue()
        with ProcessPoolExecutor() as pool:
            result_1 = pool.submit(write_queue, queue)
            pool.submit(read_queue, queue)

            wait([result_1])  # 必须要等待进程1的任务全部完成之后才能让主进程传送None给队列
            queue.put(None)


if __name__ == '__main__':
    main()
