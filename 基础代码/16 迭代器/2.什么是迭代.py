# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 20:11
# @Author  : 顾安
# @File    : 2.什么是迭代


"""
只要是可以被for循环执行的对象就是可迭代对象
"""

int_list = [1, 2, 3, 4]
for item in int_list:
    print(item)

info_dict = {
    'username': 'admin',
    'password': 123456
}

for k, v in info_dict.items():
    print(k, v)

# 整型类型不能被迭代
# number = 100
# for item in number:
#     print(item)


"""
在python中有些对象可以被迭代, 也有一些对象不能被迭代
"""

