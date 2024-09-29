# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 20:07
# @Author  : poppies
# @File    : 2.列表嵌套.py
# @Software: PyCharm


school_names = [
    ['北京大学', '清华大学'],
    ['南开大学', '天津大学', '天津师范大学'],
    ['山东大学', '中国海洋大学']
]

# 第一个索引获取的是大列表中的元素, 第二个索引是获取大列表元素[列表]中的元素
print(school_names[1][2])

# int_list = [1, 2, 3, 4]
# int_list.insert(0, ['1', '2', '3'])
# print(int_list)

print(school_names[2][0])
