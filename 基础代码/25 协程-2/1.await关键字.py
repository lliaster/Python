# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 20:04
# @Author  : 顾安
# @File    : 1.await关键字.py


"""
await可以完成任务的调度
    协程对象

    task对象
    future对象
"""

import asyncio


async def work_1():
    print('协程任务1启动...')
    # 必须等待这个任务结束后才能获取到返回值, 会造成主线程的堵塞
    res_1 = await work_2()
    res_2 = await work_3()
    print('所有任务的返回值为:', res_1, res_2)
    return '返回值1'


async def work_2():
    await asyncio.sleep(5)
    print('协程任务2启动...')
    return '返回值2'


async def work_3():
    await asyncio.sleep(5)
    print('协程任务3启动...')
    return '返回值3'

    
loop = asyncio.get_event_loop()
res = loop.run_until_complete(work_1())
print(res)

"""
1.可以使用await在一个协程函数内部运行另外一个协程任务
2.await关键字必须在一个协程函数内部
3.await关键字将任务上传到事件循环后必须获取这个任务的返回值之后才能解主线程堵塞
4.await关键字一次只能调度一个任务
5.在一个协程函数中await关键字可以出现多次

6.await与其说是任务的调度其实更加准确的是将任务上传到事件循环, 让事件循环调度任务
"""
