# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 21:37
# @Author  : 顾安
# @File    : 7.生产者消费者模式


"""
在多线程环境中可以利用队列堵塞主线程的特征来控制线程的执行步骤
"""
import threading
import time
from queue import Queue


def work_1(q):
    for i in range(1, 6):
        q.put(i)
        print('生产者:', i)
        time.sleep(2)


def work_2(q):
    # 在不明确队列内部元素个数的情况下可以用死循环
    while True:
        item = q.get()
        print(f'消费者:', item)
        # 如果消费者消费速度慢可能会导致任务未完成就被强退
        time.sleep(1.5)

        # 队列内部维护了一个任务计数器, 当队列上传一个值则计数器 + 1
        # 当任务计数器为0则可以让队列.join()方法解堵塞
        queue.task_done()  # task_done被调用一次则任务计数器 - 1


if __name__ == '__main__':
    queue = Queue()
    t1 = threading.Thread(target=work_1, args=(queue,))
    t2 = threading.Thread(target=work_2, args=(queue,))
    t2.daemon = True

    t1.start()
    t2.start()

    # 需要对有限循环的生产者任务join
    t1.join()
    queue.join()  # 当队列中的任务计数器为0时则释放主线程
    print('主程序即将结束...')

"""
1.消费者一般都是无限循环任务, 所以基本需要设置守护线程
2.生产者一般生产有限的资源, 所以基本无需设置守护线程
3.消费者因为是守护线程, 所以可能会导致消费者任务没有执行完毕就强制退出, 使用队列的任务计数器完成主线程堵塞: task_done/join
4.如果生产者生产速度过慢会导致队列任务计数器提前计算为0, 所以会在代码中让生产者线程对象join
"""
