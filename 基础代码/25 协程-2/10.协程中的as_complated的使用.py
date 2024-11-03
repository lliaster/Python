# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 22:13
# @Author  : 顾安
# @File    : 10.协程中的as_complated的使用.py

import asyncio
import random


async def work_1():
    print('开始执行任务')
    for i in range(5):
        print('执行任务中:', i)
        await asyncio.sleep(random.randint(1, 2))
    return '任务执行完毕 - 1'


async def work_2():
    print('开始执行任务')
    for i in range(5):
        print('执行任务中:', i)
        await asyncio.sleep(random.randint(1, 2))
    return '任务执行完毕 - 2'


async def work_3():
    print('开始执行任务')
    for i in range(5):
        print('执行任务中:', i)
        await asyncio.sleep(random.randint(1, 2))
    return '任务执行完毕 - 3'


async def work_4():
    print('开始执行任务')
    for i in range(5):
        print('执行任务中:', i)
        await asyncio.sleep(random.randint(1, 2))
    return '任务执行完毕 - 4'


async def main():
    tasks = [asyncio.create_task(work_1()), asyncio.create_task(work_2()), asyncio.create_task(work_3()),
             asyncio.create_task(work_4())]

    # 谁先完成谁先返回, 返回的对象是异步迭代器
    for task in asyncio.as_completed(tasks):
        result = await task
        print('任务执行结果:', result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
