# -*- coding: utf-8 -*-
# @Time    : 2024/12/10 21:13
# @Author  : 顾安
# @File    : 6.使用aiohttp获取汽车信息.py


import redis
import chardet  #判断页面编码集
import hashlib
import asyncio
import aiohttp
import aiomysql
from lxml import etree


class CarSpider:
    redis_client = redis.Redis()   #声明成类属性

    def __init__(self):
        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exf4x0/?pvareaid=102179#currengpostion' #将页面的 页数号码改成占位符
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        self.api_url = 'https://cacheapigo.che168.com/CarProduct/GetParam.ashx?specid={}'   #声明汽车详情页的url


    def __del__(self):
        self.redis_client.close()
        print('爬虫结束...')

    # 获取汽车id
    async def get_car_id(self, page, session, pool):   #定义参数:页码,请求链接对象,数据库连接池
        async with session.get(self.url.format(page), headers=self.headers) as response:  #获取汽车id的页面信息
            # 带有汽车数据的页面的编码集是GB2312
            content = await response.read()  #返回页面内容 ,而且 text默认utf-8 而且这是aiohttp包 所以这里用read()
            encoding = chardet.detect(content)['encoding']     #返回36行所读取到的页面编码集
            if encoding == 'GB2312' or encoding == 'ISO-8859-1':  #判断页面返回的编码及,因为失败页面中有gb2312编码, 所以这里需要判断一下
                result = content.decode('gbk') #@bug: 这里的编码集是gbk, 但是这里返回的页面编码集是gb2312, 所以这里需要指定编码集
                # 解析页面数据
                tree = etree.HTML(result)
                id_list = tree.xpath('//ul[@class="viewlist_ul"]/li/@specid')
                if id_list:  # 判断是否获取到数据
                    # 生成多个获取汽车信息的协程任务
                    tasks = [loop.create_task(self.get_car_info(spec_id, session, pool)) for spec_id in id_list]
                    await asyncio.wait(tasks)
                else:
                    print('id为空...')

    async def get_car_info(self, spec_id, session, pool):   #获取汽车详情页的数据
        async with session.get(self.api_url.format(spec_id), headers=self.headers) as response:  # 获取汽车详情页的数据
            result = await response.json()# 返回的是当页的一个接口信息
            if result['result'].get('paramtypeitems'):
                item = dict()
                item['name'] = result['result']['paramtypeitems'][0]['paramitems'][0]['value']  # 获取汽车名称
                item['price'] = result['result']['paramtypeitems'][0]['paramitems'][1]['value']  # 获取汽车价格
                item['brand'] = result['result']['paramtypeitems'][0]['paramitems'][2]['value']  # 获取汽车品牌
                item['altitude'] = result['result']['paramtypeitems'][1]['paramitems'][2]['value'] # 获取汽车海拔高度
                item['breadth'] = result['result']['paramtypeitems'][1]['paramitems'][1]['value']# 获取汽车宽度
                item['length'] = result['result']['paramtypeitems'][1]['paramitems'][0]['value']# 获取汽车长度
                await self.save_car_info(item, pool)
            else:
                print('数据不存在...')

    # 数据去重
    @staticmethod
    def get_md5(dict_item):
        md5 = hashlib.md5()
        md5.update(str(dict_item).encode('utf-8'))
        return md5.hexdigest()

    # 保存数据
    async def save_car_info(self, item, pool):
        # 使用异步上下文管理器创建链接对象以及游标对象
        async with pool.acquire() as conn:   #从数据库连接池中获取一个可用链接
            async with conn.cursor() as cursor:   #拿到这个链接对象后 创建一个游标对象
                val_md5 = self.get_md5(item)
                # 保存成功返回1, 保存失败返回0
                redis_result = self.redis_client.sadd('car:filter', val_md5)
                if redis_result:
                    sql = """
                                insert into car_info(
                                    id, name, price, brand, altitude, breadth, length) values (
                                        %s, %s, %s, %s, %s, %s, %s
                                    );
                            """
                    try:
                        await cursor.execute(sql, (0,
                                                   item['name'],
                                                   item['price'],
                                                   item['brand'],
                                                   item['altitude'],
                                                   item['breadth'],
                                                   item['length']
                                                   ))
                        await conn.commit()
                        print('插入成功:', item)
                    except Exception as e:
                        print('数据插入失败:', e)
                        await conn.rollback()
                else:
                    print('数据重复...')

    async def main(self):
        async with aiomysql.create_pool(user='root', password='root', db='py_spider') as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    create_table_sql = """
                                            create table car_info(
                                                id int primary key auto_increment,
                                                name varchar(100),
                                                price varchar(100),
                                                brand varchar(100),
                                                altitude varchar(100),
                                                breadth varchar(100),
                                                length varchar(100)
                                            );
                                        """

                    # 在异步代码中必须先要检查表是否存在, 直接使用if not语句无效
                    check_table_query = "show tables like 'car_info'"
                    result = await cursor.execute(check_table_query)  # 如果表存在返回1 不存在返回0
                    if not result:
                        await cursor.execute(create_table_sql)

            async with aiohttp.ClientSession() as session:
                tasks = [loop.create_task(self.get_car_id(page, session, pool)) for page in range(1, 11)]
                await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 创建事件循环对象
    car_spider = CarSpider()    # 创建/实例化  爬虫对象
    loop.run_until_complete(car_spider.main())
