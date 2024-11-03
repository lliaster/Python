# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 20:25
# @Author  : 顾安
# @File    : 2.协程环境下的同步任务.py


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
    await work_1()  # 因为await必须获取到返回值, 所以必须等待任务结束才能执行下面的任务
    await work_2()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
