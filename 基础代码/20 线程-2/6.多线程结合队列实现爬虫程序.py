# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 21:32
# @Author  : 顾安
# @File    : 6.多线程结合队列实现爬虫程序

import threading
from queue import Queue

import requests


def get_image(q):
    for _ in range(q.qsize()):
        url = q.get()
        response = requests.get(url).content

        file_name = url.rsplit('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response)
            print('下载完成...')


if __name__ == '__main__':
    url_list = [
        'http://pic.bizhi360.com/bbpic/98/10798.jpg',
        'http://pic.bizhi360.com/bbpic/92/10792.jpg',
        'http://pic.bizhi360.com/bbpic/86/10386.jpg'
    ]

    queue = Queue()
    for image_url in url_list:
        queue.put(image_url)

    t = threading.Thread(target=get_image, args=(queue,))
    t.start()
