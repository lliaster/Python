# -*- coding: utf-8 -*-
# @Time    : 2024/11/4 20:06
# @Author  : 顾安
# @File    : 2.回顾 - 在协程环境中异步执行任务.py


import asyncio


async def work_1():
    print('我是异步任务1')
    await asyncio.sleep(1)
    print('任务结束...')


async def work_2():
    print('我是异步任务2')
    await asyncio.sleep(1)
    print('任务结束...')


async def main():
    task_1 = asyncio.create_task(work_1())
    task_2 = asyncio.create_task(work_2())

    await task_1
    await task_2

loop = asyncio.get_event_loop()
loop.run_until_complete(main())