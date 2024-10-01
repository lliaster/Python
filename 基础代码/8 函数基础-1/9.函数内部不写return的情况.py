# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 21:34
# @Author  : poppies
# @File    : 9.函数内部不写return的情况.py
# @Software: PyCharm


def sub_num(num_1, num_2):
    print(num_1 - num_2)

    # 以下代码可以省略
    # 解释器会自动加上的代码
    return None

