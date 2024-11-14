# -*- coding: utf-8 -*-
# @Time    : 2024/11/11 21:49
# @Author  : 顾安
# @File    : 11.删除数据.py


import redis

with redis.Redis() as conn:
    res = conn.delete('name')
    print(res)
