# -*- coding: utf-8 -*-
# @Time     : 2024/10/26 18:15
# @Author   : Lliaster
# @File     : 多线程小爬虫.py

import threading
import time

import requests


def get_image(url):
    response = requests.get(url).content

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        print('下载完成...')


url_lst = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

start_time = time.time()
thread_lst = list()
for url in url_lst:
    t = threading.Thread(target=get_image, args=(url,))
    thread_lst.append(t)

for thread_obj in thread_lst:
    thread_obj.start()

for thread_obj in thread_lst:
    thread_obj.join()
end_time = time.time()
print('所有线程执行完毕', end_time - start_time)
