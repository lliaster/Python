# -*- coding: utf-8 -*-
# @Time    : 2024/11/11 21:39
# @Author  : 顾安
# @File    : 8.添加数据.py

# pip install redis
# 如果需要通过py文件去控制redis则不要将py文件名称设置为redis

import redis


# 1.创建链接对象
conn = redis.Redis()

# 2.添加数据: redis不需要创建所谓的游标对象
conn.set('name', '百川')

# 3.关闭链接对象
conn.close()
