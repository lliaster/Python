# -*- coding: utf-8 -*-
# @Time    : 2024/11/13 22:32
# @Author  : 顾安
# @File    : 14.删除文档.py


from pymongo import MongoClient


with MongoClient() as client:
    db = client['person']['student_info']
    # db.delete_one({'name': '张三'})

    db.delete_many({'gender': '女'})

    for item in db.find():
        print(item)


"""
今日内容最重要的部分就是数据插入: insert

"""