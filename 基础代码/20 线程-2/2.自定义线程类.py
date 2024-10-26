# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 20:12
# @Author  : 顾安
# @File    : 2.自定义线程类


import threading

import requests


class ThreadSpiderImage(threading.Thread):
    def __init__(self, image_url):
        super().__init__()
        self.image_url = image_url

    # 线程任务的运行逻辑
    def run(self):
        response = requests.get(self.image_url).content
        file_name = self.image_url.rsplit('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response)
            print('下载完成...')


if __name__ == '__main__':
    url_list = [
        'http://pic.bizhi360.com/bbpic/98/10798.jpg',
        'http://pic.bizhi360.com/bbpic/92/10792.jpg',
        'http://pic.bizhi360.com/bbpic/86/10386.jpg'
    ]

    for url in url_list:
        thread_spider = ThreadSpiderImage(url)
        thread_spider.start()
