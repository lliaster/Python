# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 21:22
# @Author  : 顾安
# @File    : 6.创建task对象的注意事项.py


import asyncio


async def others():
    print('开始任务...')
    await asyncio.sleep(2)
    print('任务结束...')
    return '测试的返回值...'


loop = asyncio.get_event_loop()

# 如果在一个协程函数外部创建task对象则必须先创建loop事件循环
# 之后使用loop对象创建task对象
tasks = [loop.create_task(others()) for _ in range(2)]

# asyncio.run(asyncio.wait(tasks))
loop.run_until_complete(asyncio.wait(tasks))
