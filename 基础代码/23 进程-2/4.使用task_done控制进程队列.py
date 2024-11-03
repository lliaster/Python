# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 20:28
# @Author  : 顾安
# @File    : 4.使用task_done控制进程队列.py

import time
from multiprocessing import Process, JoinableQueue as Queue


def write_queue(q):
    for item in [1, 2, 3]:
        q.put(item)
        print('写入的数据为:', item)
        time.sleep(0.5)


def read_queue(q):
    while True:
        item = q.get()
        print('读取的数据为:', item)
        q.task_done()


if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=write_queue, args=(queue,))
    p2 = Process(target=read_queue, args=(queue,))

    p1.start()
    # 子进程如果是守护进程则主进程不会等待守护进程的任务完成而直接退出程序
    p2.daemon = True
    p2.start()

    p1.join()  # 主进程必须等待进程1任务完成
    queue.join()  # 主进程必须等待队列任务计数器为0释放主进程
