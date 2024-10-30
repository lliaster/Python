# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 20:48
# @Author  : 顾安
# @File    : 3.线程池对象中的其他方法.py


import time
from concurrent.futures import ThreadPoolExecutor


# url = 'https://movie.douban.com/top250?start={}&filter='


def get_movie_info(movie_url):
    print(f'当前爬取的地址为: {movie_url}')
    time.sleep(3)
    return '这是测试的返回值:' + movie_url


url_1 = 'https://movie.douban.com/top250?start=0&filter='
url_2 = 'https://movie.douban.com/top250?start=25&filter='

pool = ThreadPoolExecutor(max_workers=1)
future_1 = pool.submit(get_movie_info, url_1)
future_2 = pool.submit(get_movie_info, url_2)
# print(future_1, future_2)

# 任务取消
# 任务必须在进入到线程池之前才可以取消
print('任务-2取消状态:', future_2.cancel())
print('判断任务-1是否完成:', future_1.done())
print('判断任务-2是否完成:', future_2.done())

# 获取任务的返回值
print(future_1.result())
# print(future_2.result())
