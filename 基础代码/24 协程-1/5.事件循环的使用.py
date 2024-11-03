# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 21:54
# @Author  : 顾安
# @File    : 5.事件循环的使用.py

import asyncio
import time


# 异步任务1
async def work_1():
    for _ in range(5):
        print('我是异步任务1')
        # 模拟耗时操作, 在协程环境中不能用time.sleep()
        # 协程任务调度如果遇到了耗时的任务则会自动切换到下一个任务
        await asyncio.sleep(1)


# 异步任务2
async def work_2():
    for _ in range(5):
        print('我是异步任务2')
        await asyncio.sleep(1)


tasks = [
    work_1(),
    work_2()
]

# 创建事件循环对象-1: 当前创建的方式适合python3.6 - python3.9版本以及Windows操作系统
loop = asyncio.get_event_loop()

# 使用事件循环对象中的run_until_complete方法完成任务的调度
# run_until_complete只能接收可等待对象: 协程对象、Future对象、Task对象
# wait()方法返回一个可等待对象并可以接收任务列表
start_time = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print('耗时:', end_time - start_time)

# 创建事件循环对象-2: 适合Linux系统以及python3.10以上版本的解释器
# asyncio.run(asyncio.wait(tasks))
