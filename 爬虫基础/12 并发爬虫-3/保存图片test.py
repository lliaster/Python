# -*- coding: utf-8 -*-
# @Time     : 2024/12/15 16:01
# @Author   : Lliaster
# @File     : 保存图片test.py


# -*- coding: utf-8 -*-
# @Time     : 2024/12/15 00:12
# @Author   : Lliaster
# @File     : 网站图片并保存_线程.py


import os
from fake_useragent import UserAgent  # 随机UA池
import requests
from lxml import etree
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed  # 导入线程池

url = 'https://www.lpbzj.vip/allimg/page/{}'
all_image_info = []



def get_url_pageNum():
    user_agent = UserAgent()
    response = requests.get('https://www.lpbzj.vip/allimg', headers={'User-Agent': user_agent.random}).text
    tree = etree.HTML(response)
    max_page = tree.xpath("//div[@class='pagination']//li[last()-2]/a/text()")
    return max_page[0]


def get_image_info_url(q, page):
    user_agent = UserAgent()
    for i in range(1, int(page) + 1):
        response = requests.get(url.format(i), headers={'User-Agent': user_agent.random}).text
        tree = etree.HTML(response)
        image_info = tree.xpath('//h3[@itemprop="name headline"]/a[@rel="bookmark"]/@href')
        q.put(image_info)
        all_image_info.append(image_info)# 将数据放入队列中
    print(all_image_info)

def process_image_info(info_url):
    try:
        user_agent = UserAgent()
        response = requests.get(info_url, headers={'User-Agent': user_agent.random}).text
        tree = etree.HTML(response)
        title= tree.xpath('//title/text()')
        imagedown_urls = tree.xpath('//img[@src and @class="aligncenter"]/@src')
        for img_url in imagedown_urls:
            get_image(img_url,title[0])
            print('标题为:{}下载链接:{}'.format(title, img_url))
    except Exception as e:
            print('获取链接失败',info_url)

def get_image_url(q):
    with ThreadPoolExecutor(max_workers=20) as executor:  # 设置最大线程数
        futures = []
        while True:
            info_url = q.get()
            if info_url is None:
                break
            for temp in info_url:
                future = executor.submit(process_image_info, temp)
                futures.append(future)
            q.task_done()
        for future in as_completed(futures):
            future.result()

def get_image(url,title):
    try:
        response = requests.get(url).content
        title = title.replace("'", "").replace("[", "").replace("]", "").replace(" ", "").replace("百度云网盘-老婆不在家", "")
        imgpath = os.path.join(r'D:\爬虫图片', title)
        if not os.path.exists(imgpath):
            os.makedirs(imgpath)
        file_path = os.path.join(imgpath, url.rsplit('/')[-1])
        print('file_path:', file_path)
        with open(file_path, 'wb') as f:
            f.write(response)
            print(f'下载完成: {file_path}')
    except Exception as e:
        print('下载图片失败',url,title)


if __name__ == '__main__':
    queue = Queue()
    page = get_url_pageNum()
    # page = 1
    t1 = threading.Thread(target=get_image_info_url, args=(queue, page))
    t2 = threading.Thread(target=get_image_url, args=(queue,))
    t2.daemon = True
    t1.start()
    t2.start()
    t1.join()
    queue.join()
    queue.put(None)  # 添加结束标志，通知 t2 结束
    t2.join()
