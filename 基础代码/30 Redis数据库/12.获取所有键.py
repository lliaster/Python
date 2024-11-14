# -*- coding: utf-8 -*-
# @Time    : 2024/11/11 21:50
# @Author  : 顾安
# @File    : 12.获取所有键.py


import redis

with redis.Redis() as conn:
    res = conn.keys()
    for item in res:
        print(item.decode())


