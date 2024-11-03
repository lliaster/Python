# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 20:39
# @Author  : 顾安
# @File    : 5.进程池的实现方式 - 1（不常用）.py


import random
import time
from multiprocessing import Pool


def work(proc_name, *args, **kwargs):
    p_start = time.time()
    print(f'{proc_name}开始执行...')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    time.sleep(random.randint(1, 2))
    p_end = time.time()
    print(f'{proc_name}执行完毕, 耗时: {p_end - p_start}')


if __name__ == '__main__':
    # 设置进程池的进程数量
    pool = Pool(3)

    for item in range(1, 11):
        # 任务同步调度
        # pool.apply(work, (item, '测试参数-1', '测试参数-2'), {'people_name': '安娜'})

        # 任务并发调度
        pool.apply_async(work, (item, '测试参数-1', '测试参数-2'), {'people_name': '安娜'})

    # 关闭进程池
    pool.close()

    # 等待进程池中的任务全部执行完毕
    # close必须在join之前调用
    pool.join()
