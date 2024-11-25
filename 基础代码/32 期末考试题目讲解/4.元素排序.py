# -*- coding: utf-8 -*-
# @Time    : 2024/11/20 20:32
# @Author  : 顾安
# @File    : 4.元素排序.py


lst = [7, -8, 5, 4, 0, -2, -5]

# x < 0返回的是布尔值, False在前, True在后
new_lst = sorted(lst, key=lambda x: (x < 0, x if x >= 0 else -x))

# new_lst = sorted(lst, key=lambda x: (x < 0, abs(x)))
# print(new_lst)
