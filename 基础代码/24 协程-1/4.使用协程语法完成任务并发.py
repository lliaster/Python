# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 21:44
# @Author  : 顾安
# @File    : 4.使用协程语法完成任务并发.py


import asyncio


async def work_1():
    for _ in range(5):
        print('异步任务-1')


async def work_2():
    for _ in range(5):
        print('异步任务-2')


# 创建任务列表
tasks = [
    work_1(),
    work_2()
]

# 创建事件循环对象
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
