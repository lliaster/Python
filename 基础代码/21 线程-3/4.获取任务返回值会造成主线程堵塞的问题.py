# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 21:06
# @Author  : 顾安
# @File    : 4.获取任务返回值会造成主线程堵塞的问题.py


import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint

url = 'https://movie.douban.com/top250?start={}&filter='


def get_movie_info(movie_url):
    print(f'当前爬取的地址为: {movie_url}')
    time.sleep(randint(1, 2))
    return '这是一个测试的返回值:' + movie_url


# 1.创建线程池对象
pool = ThreadPoolExecutor()

# 2.提交任务
future_list = [pool.submit(get_movie_info, url.format(page * 25)) for page in range(10)]

print('-' * 30)

# 3.获取每个future对象的返回值, 如果获取返回值没有as_completed则顺序返回
for future in as_completed(future_list):
    # for future in future_list:
    print(future.result())  # result方法会让主线程堵塞

# 4.程序结束
print('主程序结束...')

"""
1.获取任务返回值的过程中会堵塞主线程: future.result()
2.在没有使用as_completed方法时直接打印多个任务的返回值是根据你提交任务的顺序决定的

as_completed
    可以将一个可迭代对象转为一个生成器
        谁先完成任务谁就先返回具体的结果
"""
