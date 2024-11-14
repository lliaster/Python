# -*- coding: utf-8 -*-
# @Time    : 2024/11/13 22:23
# @Author  : 顾安
# @File    : 11.链接数据库.py

# pip install pymongo
from pymongo import MongoClient

# 1.创建链接对象
mongo_client = MongoClient()

# 2.链接指定数据库
db = mongo_client['person']

# 3.关闭链接对象
mongo_client.close()
