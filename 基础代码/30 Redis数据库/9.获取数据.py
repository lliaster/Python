# -*- coding: utf-8 -*-
# @Time    : 2024/11/11 21:45
# @Author  : 顾安
# @File    : 9.获取数据.py


import redis

with redis.Redis() as conn:
    result = conn.get('name')
    print(result.decode())  # 如果在windows中解码返回的数据还是乱码则设置成gbk编码

