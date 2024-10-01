# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 20:27
# @Author  : poppies
# @File    : 3.range的使用.py
# @Software: PyCharm


"""
range 类型表示不可变的数字序列，通常用于在 for 循环中循环指定的次数。
"""


obj_1 = range(5)
print(list(obj_1))

obj_2 = range(1, 5)
print(list(obj_2))

obj_3 = range(1, 11, 3)
print(list(obj_3))


obj_4 = range(0, -10, -1)
print(list(obj_4))

obj_5 = range(11, 0, -1)
print(list(obj_5))



