# -*- coding: utf-8 -*-
# @Time    : 2024/11/4 20:57
# @Author  : 顾安
# @File    : 7.异步上下文管理器.py

import asyncio


# 模拟数据库增删改查
class AsyncContextManager:
    def __init__(self, conn):
        print(1)
        self.conn = conn

    async def read_info(self):
        print(3)
        print('模拟打印数据库连接对象:', self.conn)
        print('正在模拟读取数据库内容...')
        await asyncio.sleep(1)

    async def __aenter__(self):
        print(2)
        # 模拟创建数据库连接对象
        self.conn = await asyncio.sleep(1, result='模拟创建一个数据库连接对象')
        print(self.conn)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(4)
        self.conn = await asyncio.sleep(1, result='模拟关闭一个数据库连接对象')
        print(self.conn)


async def main():
    async with AsyncContextManager(None) as acm:
        await acm.read_info()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())