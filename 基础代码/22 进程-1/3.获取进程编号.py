# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 21:57
# @Author  : 顾安
# @File    : 3.获取进程编号.py


import multiprocessing
import os


def run_process():
    print(f'子进程的编号为: {os.getpid()}')
    print(f'子进程打印的主进程的编号为: {os.getppid()}')


if __name__ == '__main__':
    p = multiprocessing.Process(target=run_process)
    p.start()
    p.join()

    print('主进程自身打印的编号为:', os.getpid())
