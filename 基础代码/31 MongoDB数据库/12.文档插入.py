# -*- coding: utf-8 -*-
# @Time    : 2024/11/13 22:26
# @Author  : 顾安
# @File    : 12.文档插入.py


from pymongo import MongoClient

with MongoClient() as client:
    db = client['person']['student_info']

    student_info_list = [
        {"name": "张三", "age": 18, "gender": "男"},
        {"name": "李四", "age": 20, "gender": "男"},
        {"name": "王五", "age": 19, "gender": "女"},
        {"name": "赵六", "age": 22, "gender": "男"},
        {"name": "钱七", "age": 23, "gender": "女"}
    ]

    db.insert_many(student_info_list)
