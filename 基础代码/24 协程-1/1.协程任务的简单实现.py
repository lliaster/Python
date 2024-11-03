# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 21:25
# @Author  : 顾安
# @File    : 1.协程任务的简单实现.py


import asyncio


# async: 用于定义协程函数的关键字
async def work():
    print('hello world')


# 协程函数名称后添加小括号会返回一个对象: 协程对象
# coro_obj = work()
# print(coro_obj)

asyncio.run(work())

"""
1.获取定义的协程函数返回的协程对象: 协程对象 = 协程函数()
2.将协程对象放到asyncio模块的run方法去调度执行
"""
