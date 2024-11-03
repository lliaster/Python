# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 21:27
# @Author  : 顾安
# @File    : 7.asyncio中的future对象.py


import asyncio


# async def others():
#     print('协程任务启动...')
#     await asyncio.sleep(2)
#     print('协程任务完成...')
#     return '123'
#
#
# loop = asyncio.get_event_loop()
# future_list = [asyncio.ensure_future(others()) for _ in range(2)]
# results = loop.run_until_complete(asyncio.gather(*future_list))
# print(results)


async def set_return(future):
    await asyncio.sleep(2)
    future.set_result('这是我们自己设置的返回值...')


async def main():
    # 1.获取一个正在运行的事件循环对象
    loop_obj = asyncio.get_running_loop()

    # 2.使用获取的事件循环创建一个future对象
    fut = loop_obj.create_future()

    # 3.设置future返回值
    # fut.set_result('这是我们自己设置的返回值...')
    await loop_obj.create_task(set_return(fut))

    # 4.使用 await 等待 future 对象的结果
    res = await fut

    print(res)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

"""
asyncio.get_event_loop(): 获取一个事件循环, 如果事件循环不存在则创建一个新的事件循环
asyncio.get_running_loop(): 获取一个正在运行的事件循环, 如果没有则直接报错
asyncio.set_event_loop(): 设置一个事件循环对象
asyncio.new_event_loop(): 创建一个新的事件循环, 如果已经存在也会创建一个新的事件循环对象
"""
