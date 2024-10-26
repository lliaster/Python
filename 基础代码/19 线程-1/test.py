# -*- coding: utf-8 -*-
# @Time     : 2024/10/26 17:32
# @Author   : Lliaster
# @File     : test.py
import threading
import time

import requests


def work1():
    for i in range(6):
        print(int(time.time()), i)
        time.sleep(1)


def work2():
    for i in range(6, 11):
        print(int(time.time()), i)
        time.sleep(1)


t1 = threading.Thread(target=work1)
t2 = threading.Thread(target=work2)

# t1.start()
# t2.start()
print('\n小爬虫实例', 'X' * 55)


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
for i in url_lst:
    get_image(i)
end_time = time.time()
print(end_time - start_time, '下载完成')
