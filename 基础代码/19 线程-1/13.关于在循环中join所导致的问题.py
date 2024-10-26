# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 22:09
# @Author  : 顾安
# @File    : 13.关于在循环中join所导致的问题


import threading
import time


def work():
    for i in range(1, 6):
        print(i)
        time.sleep(3)


t1 = threading.Thread(target=work)
t2 = threading.Thread(target=work)
t3 = threading.Thread(target=work)

thread_list = [t1, t2, t3]
for thread_obj in thread_list:
    thread_obj.start()
    thread_obj.join()  # 在for循环中启动线程和线程join会导致后面的线程必须等待前一个线程任务完成后才能被启动

#
# for thread_obj in thread_list:
#     thread_obj.join()
