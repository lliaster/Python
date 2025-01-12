# -*- coding: utf-8 -*-
# @Time    : 2025/1/7 20:31
# @Author  : 顾安
# @File    : insert_start_url.py


import redis


with redis.Redis(host='192.168.18.6', port=6379, db=0) as redis_client:
    redis_client.lpush('dd_book:start_urls', 'https://search.dangdang.com/?key=Python&act=input&page_index=1')
