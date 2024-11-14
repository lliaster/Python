# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 20:35
# @Author  : 顾安
# @File    : 4.task对象.py


"""
协程对象本身不参与任务并发
    如果想要多个任务实现并发则需要将协程对象打包成task对象

    task对象才支持异步并发
"""

import asyncio


async def others():
    print('开始任务...')
    await asyncio.sleep(2)
    print('任务结束...')
    return '测试的返回值...'


async def main():
    """
    在main函数中调度其他的协程任务完成并发
    """
    task_1 = asyncio.create_task(others())
    task_2 = asyncio.create_task(others())

    # await后面如果后面跟的是task对象，那么task对象会被立即调度执行，并且返回task对象执行结果
    # res_1 = await task_1
    # res_2 = await task_2
    # print(res_1, res_2)

    # 将多个task对象存储到一个任务列表中
    task_list = [task_1, task_2]

    # 批量上传任务有两种方式: asyncio.wait / asyncio.gather
    # gather方法只能接收可等待对象
    # gather方法无法直接接收列表类型, 需要进行解包

    # res_list = await asyncio.wait(task_list)
    res_list = await asyncio.gather(task_1, task_2)
    res_list = await asyncio.gather(*task_list)  # 返回值是一个列表
    print(res_list)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
