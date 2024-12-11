# -*- coding: utf-8 -*-
# @Time     : 2024/12/11 20:32
# @Author   : Lliaster
# @File     : 测试.py


import asyncio


def my_callback(obj):
    print('回调函数执行了')
    print(obj.result())
    print('回调函数结束了')


async def work():
    print('异步任务执行了')
    await asyncio.sleep(1)
    print('异步任务结束了')
    return '回调函数返回值'


loop = asyncio.get_event_loop()
task_obj = loop.create_task(work())
task_obj.add_done_callback(my_callback)
loop.run_until_complete(task_obj)
