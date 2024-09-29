# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 21:22
# @Author  : poppies
# @File    : 11.使用匿名函数完成列表元素排序.py
# @Software: PyCharm


stu_list = [
    {"name": "顾安", "age": 18},
    {"name": "夏洛", "age": 19},
    {"name": "木木", "age": 17}
]

# def my_sort(item):
#     return item["age"]

# stu_list.sort(key=my_sort, reverse=True)
# print(stu_list)

stu_list.sort(key=lambda item: item['age'], reverse=True)
print(stu_list)


# class MyList:
#     def __init__(self, list_data):
#         self.list_data = list_data
#
#     def sort(self, key):
#         for item in self.list_data:
#             result = key(item)
#             print(result)
#
#
# my_list = MyList([1, 2, 3, 4, 5])
# my_list.sort(lambda item: item)

