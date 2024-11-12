# -*- coding: utf-8 -*-
# @Time    : 2024/11/4 20:41
# @Author  : 顾安
# @File    : 5.异步生成器.py


import asyncio


async def work():
    for item in range(1, 101):
        yield item


async def main():
    async for item in work():
        print(item)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
