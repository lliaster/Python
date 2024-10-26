# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:57
# @Author  : 顾安
# @File    : 8.多线程爬虫任务

import threading
import time

import requests


def get_image(url):
    response = requests.get(url).content

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

start_time = time.time()
thread_list = list()
for url in url_list:
    t = threading.Thread(target=get_image, args=(url,))
    thread_list.append(t)

for thread_obj in thread_list:
    thread_obj.start()
    # thread_obj.join()  启动第一个线程之后直接堵塞主线程会导致后续的任务无法启动

# 重新遍历所有的线程对象再让主线程等待
for thread_obj in thread_list:
    thread_obj.join()

end_time = time.time()
print('耗时:', end_time - start_time)
