# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 21:49
# @Author  : poppies
# @File    : 6.缺省参数的设置规则.py
# @Software: PyCharm


"""
缺省参数必须在形式参数之后
"""


def print_info(name, age=18, address='长沙'):
    print(name, age, address)


print_info('安娜')
