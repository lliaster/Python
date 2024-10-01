# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 21:35
# @Author  : poppies
# @File    : 10.容器类型互转.py
# @Software: PyCharm


str_data = 'abcdef'
str_list = list(str_data)
print(str_list)

str_set = set(str_list)
print(str_set)

str_tuple = tuple(str_set)
print(str_tuple)

# 无法将列表、字典、集合中的元素转为字符串
# str_data = str(str_tuple)
# print(str_data)

"""
当前案例并没有包含字典类型, 字典类型比较特殊
"""



