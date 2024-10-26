# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:56
# @Author  : 顾安
# @File    : 7.单线程同步爬虫任务

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
for url in url_list:
    get_image(url)
end_time = time.time()
print('耗时:', end_time - start_time)
