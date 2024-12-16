# -*- coding: utf-8 -*-
# @Time     : 2024/12/15 00:12
# @Author   : Lliaster
# @File     : 网站图片并保存_线程.py



"""
家庭作业:
    1.将上述代码修改成进程池
        在进程池中需要使用Manager创建队列对象

    2.使用线程的方式获取网站图片并保存
        请求地址: https://www.lpbzj.vip/allimg
        要求: 进入到详情页并获取所有图片资源并保存到本地

        作业完成后截图你保存的图片文件夹私发企业微信即可！！！
"""




import redis
import chardet
import hashlib
from lxml import etree
from fake_useragent import UserAgent                     #随机UA池
import requests
from lxml import etree
import threading
import time
from queue import Queue

from concurrent.futures import ThreadPoolExecutor, as_completed   #导入线程池

url = 'https://www.lpbzj.vip/allimg/page/{}'
all_image_info = []
def get_url_pageNum():
    user_agent = UserAgent()
    response = requests.get('https://www.lpbzj.vip/allimg', headers={'User-Agent': user_agent.random}).text
    tree = etree.HTML(response)
    max_page = tree.xpath("//div[@class='pagination']//li[last()-2]/a/text()")
    return max_page[0]

def get_image_info_url(q,page):
    user_agent = UserAgent()
    for i in range(1, int(page)+1):
        response = requests.get(url.format(i), headers={'User-Agent': user_agent.random}).text
        tree = etree.HTML(response)
        image_info = tree.xpath('//h3[@itemprop="name headline"]/a[@rel="bookmark"]/@href')
        q.put(image_info) # 将数据放入队列中
        # all_image_info.append(image_info)
    print(all_image_info)

def get_image_url(q):
    while True:
        info_url = q.get()   # 从队列中取出数据
        if info_url is not None:
            for  temp in info_url:
                user_agent = UserAgent()
                response = requests.get(temp, headers={'User-Agent': user_agent.random}).text
                tree = etree.HTML(response)
                title = tree.xpath('//title/text()')
                imagedown_url = tree.xpath('//img[@src and @class="aligncenter"]/@src')
                print(imagedown_url)


def get_image(url):
    response = requests.get(url).content

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        print('下载完成...')


if __name__ == '__main__':
    queue = Queue()
    page = get_url_pageNum()
    t1 = threading.Thread(target=get_image_info_url, args=(queue,page))
    t2 = threading.Thread(target=get_image_url, args=(queue,))
    t2.daemon = True
    t1.start()
    t2.start()
    t1.join()
    queue.join()