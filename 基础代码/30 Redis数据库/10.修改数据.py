# -*- coding: utf-8 -*-
# @Time    : 2024/11/11 21:48
# @Author  : 顾安
# @File    : 10.修改数据.py


import redis

with redis.Redis() as conn:
    conn.set('name', '安娜')
    print(conn.get('name').decode())
