# -*- coding: utf-8 -*-
# @Time    : 2024/11/4 20:10
# @Author  : 顾安
# @File    : 3.task对象的特征.py


import asyncio


async def work():
    print('我是一个协程函数')
    await asyncio.sleep(1)
    print('任务结束...')


async def main():
    task = asyncio.create_task(work())
    # 获取任务的返回值， 让主线程堵塞
    await task


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

"""
1.asyncio内置标准库
2.async关键字
3.loop = asyncio.get_event_loop()创建事件循环负责任务的调度执行
4.run_until_complete执行任务
5.await关键字
6.task对象的创建
7.future对象的创建
8.run_in_executor执行不支持协程环境的代码: 本质是线程池
9.任务返回值的获取: wait / gather
"""
