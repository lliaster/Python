# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 21:43
# @Author  : 顾安
# @File    : 1.进程的简单使用.py


import multiprocessing


def work():
    for i in range(1, 6):
        print('我被执行了:', i)


# 启动进程需要在函数入口下执行
if __name__ == '__main__':
    # 1.创建进程对象
    p = multiprocessing.Process(target=work)

    # 2.启动进程
    p.start()
