# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 20:56
# @Author  : 顾安
# @File    : 5.wait方法.py


"""
在协程环境中批量上传任务可以使用wait方法或gather方法
    wait: wait方法可以接收一个可迭代对象, 返回值是一个元组, 元组中有两个元素, 都是集合类型
"""

import asyncio


async def work():
    print('协程任务...')
    await asyncio.sleep(4)
    return '测试的返回值...'


async def main():
    tasks = [asyncio.create_task(work(), name=f'自定义协程{_}') for _ in range(1, 3)]
    done, pending = await asyncio.wait(tasks)
    print(done, pending)
    for item in done:
        print(item.result())
        print(item.get_name())


# loop: 事件循环对象（用于任务的异步调度）
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
