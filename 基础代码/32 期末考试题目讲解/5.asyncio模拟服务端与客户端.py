# -*- coding: utf-8 -*-
# @Time    : 2024/11/20 20:47
# @Author  : 顾安
# @File    : 5.asyncio模拟服务端与客户端.py


"""
使用 Python 的asyncio库来实现协程
创建服务器协程，模拟不同任务的处理时间
创建多个客户端协程，向服务器发送请求
使用asyncio.gather来并发执行客户端协程，并记录开始时间和结束时间以计算总时间
"""

import time
import asyncio
from random import randint


async def server_coroutine(task_id, task_time):
    await asyncio.sleep(task_time)
    return f'任务 - {task_id} 在 {task_time} 秒内完成'


async def client_request(task_id, task_time):
    response = await server_coroutine(task_id, task_time)
    return response


async def main():
    create_client = 5
    tasks = list()
    task_time_list = [randint(1, 6) for _ in range(5)]
    print(task_time_list)
    for i in range(create_client):
        tasks.append(asyncio.create_task(client_request(i + 1, task_time_list[i])))

    # gather是顺序返回的
    response = await asyncio.gather(*tasks)
    # response = await asyncio.gather(*asyncio.as_completed(tasks))
    for res in response:
        print(res)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print('总耗时:', end_time - start_time)

