# -*- coding: utf-8 -*-
# @Time    : 2024/11/4 20:32
# @Author  : 顾安
# @File    : 4.异步迭代器.py


import asyncio


class MyAsyncReader:
    def __init__(self):
        self.count = 0

    # 模拟文件的异步读取
    async def read_line(self):
        self.count += 1
        if self.count == 101:
            return None
        return self.count

    # 不是异步函数
    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.read_line()
        if value is None:
            raise StopAsyncIteration
        return value


async def main():
    async for item in MyAsyncReader():
        print(item)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
