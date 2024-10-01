# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 21:46
# @Author  : poppies
# @File    : 11.通过return返回多个值.py
# @Software: PyCharm


def return_num():
    return 1, 2, 3  # 如果return返回多个值则会将这些值打包成一个元组


result = return_num()
print(result)

r1, r2, r3 = return_num()
print(r1, r2, r3)

