# -*- coding: utf-8 -*-
# @Time    : 2024/11/4 20:45
# @Author  : 顾安
# @File    : 6.绑定回调.py

import asyncio


# 回调函数
def callback(future):
    print(f'回调函数执行了: {future.result()}')


async def send_message(content):
    await asyncio.sleep(1)
    print(f'信息内容:', content)
    return f'返回值: {content}'


async def main():
    # task = asyncio.create_task(send_message('hello world'))
    # result = await asyncio.gather(task)
    # print(result[0])

    # result = await task
    # print(result)

    task_list = [asyncio.create_task(send_message(f'这是一个测试信息: {item}')) for item in range(1, 11)]

    for task in task_list:
        # 当任务执行完毕之后会执行绑定的回调函数
        task.add_done_callback(callback)
    await asyncio.gather(*task_list)
#asyncio.gather  的意思是收集所有任务的返回值形成一个列表;返回的值和原来提交的任务保持一致，但是过程是异步的

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
