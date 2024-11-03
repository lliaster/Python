# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 20:30
# @Author  : 顾安
# @File    : 3.协程环境下的并发任务.py


import asyncio


async def work_1():
    for i in range(5):
        print('work_1:', i)
        await asyncio.sleep(2)


async def work_2():
    for i in range(5):
        print('work_2:', i)
        await asyncio.sleep(2)


async def main():
    coro_list = [work_1(), work_2()]
    # 在python解释器高版本当中无法直接将协程对象批量上传到事件循环对象中, 需要使用task对象
    await asyncio.wait(coro_list)  # 使用wait方法批量上传任务到事件循环对象


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
