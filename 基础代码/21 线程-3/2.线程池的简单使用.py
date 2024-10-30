# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 20:28
# @Author  : 顾安
# @File    : 2.线程池的简单使用.py

import time
from concurrent.futures import ThreadPoolExecutor

url = 'https://movie.douban.com/top250?start={}&filter='


def get_movie_info(movie_url):
    print(f'当前爬取的地址为: {movie_url}')
    time.sleep(3)


# 1.创建线程池对象
pool = ThreadPoolExecutor()

# 2.提交任务
for page in range(10):
    pool.submit(get_movie_info, url.format(page * 25))

"""
1.对ThreadPoolExecutor类进行实例化并获取线程池对象
    线程池一旦创建则就存在一定数量的线程对象

2.使用线程池对象中的submit完成任务提交

线程池最大的好处是线程对象复用
"""
