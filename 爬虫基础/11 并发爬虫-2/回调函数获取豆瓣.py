# -*- coding: utf-8 -*-
# @Time     : 2024/12/11 21:02
# @Author   : Lliaster
# @File     : 回调函数获取豆瓣.py




import asyncio
import aiohttp
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start={}&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}


def my_callback(task):
    print(task.result())


async def get_movie_info(page_num):
    # 1.使用异步上下文管理器创建请求对象以及响应对象
    async with aiohttp.ClientSession() as session:
        async with session.get(url.format(page_num), headers=headers) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            div_list = soup.find_all('div', class_='hd')
            for title in div_list:
                # print(title.get_text())
                return title.get_text()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(get_movie_info(page * 25)) for page in range(10)]
    for task in tasks:
        task.add_done_callback(my_callback)
    loop.run_until_complete(asyncio.wait(tasks))
