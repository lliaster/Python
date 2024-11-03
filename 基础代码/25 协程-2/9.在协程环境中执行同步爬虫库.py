# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 21:51
# @Author  : 顾安
# @File    : 9.在协程环境中执行线程任务.py


import asyncio

# requests是一种同步爬虫库, 本身不支持协程
import requests


async def get_image(url):
    print('开始下载...')
    # response = requests.get(url).content
    future = loop.run_in_executor(None, requests.get, url)
    response = await future

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)
        print('下载完成...')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    url_list = [
        'http://pic.bizhi360.com/bbpic/98/10798.jpg',
        'http://pic.bizhi360.com/bbpic/92/10792.jpg',
        'http://pic.bizhi360.com/bbpic/86/10386.jpg'
    ]

    task_list = [loop.create_task(get_image(url)) for url in url_list]
    loop.run_until_complete(asyncio.wait(task_list))

"""
如果一个第三方库必须要运行在协程环境中, 则可以run_in_executor在协程环境运行
    以上方法本质还是线程执行
"""

"""
1.await关键字的使用
2.await关键字的特征: 执行协程对象会堵塞代码, 执行task对象是并发执行
3.如何创建task对象
4.wait方法的使用
5.gather方法的使用
6.线程池中的future和协程中的future的不同点
"""
