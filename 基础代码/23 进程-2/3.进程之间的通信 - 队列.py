# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 20:20
# @Author  : 顾安
# @File    : 3.进程之间的通信 - 队列.py


import time
from multiprocessing import Process, Queue


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


if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=write_queue, args=(queue,))
    p2 = Process(target=read_queue, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None)

"""
进程之间的数据共享可以使用队列的方式完成
    from multiprocessing import Queue
"""
