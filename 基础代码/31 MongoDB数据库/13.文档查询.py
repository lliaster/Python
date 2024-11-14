# -*- coding: utf-8 -*-
# @Time    : 2024/11/13 22:29
# @Author  : 顾安
# @File    : 13.文档查询.py

from pymongo import MongoClient

with MongoClient() as client:
    db = client['person']['student_info']
    print(db.find())  # 返回的对象支持迭代和强转(list)

    # for item in db.find():
    #     print(item)

    # print(list(db.find()))

    result = db.find_one()
    print(result)

