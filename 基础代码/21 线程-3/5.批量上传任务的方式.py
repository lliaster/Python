# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 21:19
# @Author  : 顾安
# @File    : 5.批量上传任务的方式.py


import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint

url = 'https://movie.douban.com/top250?start={}&filter='


def get_movie_info(movie_url):
    print(f'当前爬取的地址为: {movie_url}')
    time.sleep(randint(1, 2))
    return '这是一个测试的返回值:' + movie_url


# max_workers: 定义最大线程数
pool = ThreadPoolExecutor()
url_list = [url.format(i * 25) for i in range(10)]

# map方法会返回一个迭代器对象, map的第二个参数需要传递一个可迭代对象
futures = pool.map(get_movie_info, url_list)

print('-' * 30)

# 直接对迭代器进行迭代并直接获取结果, 无需使用result()
# 返回的结果顺序和上传任务的顺序保持一致
for item in futures:
    print(item)

for item in as_completed(futures):
    print(item)
