# -*- coding: utf-8 -*-
# @Time    : 2024/12/15 21:41
# @Author  : 顾安
# @File    : 5.使用协程完成王者荣耀图片下载.py


import os
import asyncio
import aiofile
import aiohttp


class HeroSkin:
    def __init__(self):
        self.json_url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

    async def get_image_content(self, session, e_name, c_name):  #session是aio http创建的一个对象
        for skin_id in range(1, 31):
            async with session.get(self.skin_url.format(e_name, e_name, skin_id), headers=self.headers) as response:
                if response.status == 200:
                    content = await response.read()
                    async with aiofile.async_open('./images/' + c_name + '-' + str(skin_id) + '.jpg', 'wb') as f:
                        await f.write(content)
                        print('写入成功:', c_name)
                else:
                    break

    async def main(self):
        task_list = list() # 用来存放所有的任务对象
        async with aiohttp.ClientSession() as session:  # 创建一个session对象
            async with session.get(self.json_url, headers=self.headers) as response:   # 获取json数据
                result = await response.json(content_type=None)  #因为json_url返回的是一个文件,所以不用设置编码
                for item in result:  # 遍历json数据
                    e_name = item['ename']     # 英文名
                    c_name = item['cname']      # 中文名
                    coro_obj = self.get_image_content(session, e_name, c_name)    # 创建一个协程对象


                    # task_list.append(asyncio.create_task(coro_obj))   # 创建一个任务对象

                    # 如果在windows上执行asyncio.create_task报错则将asyncio替换成loop执行
                    task_list.append(loop.create_task(coro_obj))

                await asyncio.wait(task_list)                                # 等待所有任务完成


if __name__ == '__main__':
    loop = asyncio.get_event_loop()   # 创建一个事件循环

    if not os.path.exists('./images/'):  # 判断文件夹是否存在
        os.mkdir('./images/')       # 创建文件夹

    hero_skin = HeroSkin()      # 创建一个对象
    # asyncio.run(hero_skin.main())    # 执行异步代码

    loop.run_until_complete(hero_skin.main())

    """
    家庭作业:
        将照片图集(线程池版本)中的代码修改成异步协程版本
    """
