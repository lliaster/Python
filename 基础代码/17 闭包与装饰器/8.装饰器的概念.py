# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 21:06
# @Author  : 顾安
# @File    : 8.装饰器的概念


import time
import requests


def spider_time(spider_func):
    def wrapper():
        start_time = time.time()
        spider_func()  # 在内部函数中直接执行外层函数接收到的爬虫函数
        end_time = time.time()
        print('耗时:', end_time - start_time)

    return wrapper


@spider_time
def spider_baidu():
    url = 'https://www.baidu.com'
    response = requests.get(url)
    time.sleep(2)
    print(response.content.decode())


@spider_time
def spider_google():
    url = 'https://www.google.com'
    response = requests.get(url)
    time.sleep(2)
    print(response.text)


spider_baidu()
spider_google()

"""
装饰器的本质功能:不修改原有功能代码结构的基础上添加其他功能
"""
