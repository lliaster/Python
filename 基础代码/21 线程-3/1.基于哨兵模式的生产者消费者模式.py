# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 20:09
# @Author  : 顾安
# @File    : 1.基于哨兵模式的生产者消费者模式.py


import threading
import time
from queue import Queue


def work_1(q, name):
    for i in range(1, 11):
        q.put(i)
        print(f'生产者-{name}生产了: {i}')
        time.sleep(0.5)


def work_2(q, name):
    while True:
        item = q.get()
        if item is not None:
            print(f'消费者-{name}请求了: {item}')
            time.sleep(0.7)
        else:
            break


if __name__ == '__main__':
    queue = Queue()
    t1 = threading.Thread(target=work_1, args=(queue, '南枫'))
    t2 = threading.Thread(target=work_2, args=(queue, '百川'))

    # 使用哨兵模式不需要创建消费者守护线程
    t1.start()
    t2.start()

    t1.join()
    # 使用主线程在队列中推送哨兵信号
    queue.put(None)

    t2.join()
    # 使用主线程打印程序结束信息
    print('主程序结束...')
