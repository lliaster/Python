# -*- coding: utf-8 -*-
# @Time    : 2024/11/4 20:02
# @Author  : 顾安
# @File    : 1.回顾 - 在协程环境中同步执行任务.py


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
    coro_obj_1 = work_1()
    coro_obj_2 = work_2()

    # await 调度任务并获取返回值之后整个main程序才会继续向下执行
    await coro_obj_1
    await coro_obj_2

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
