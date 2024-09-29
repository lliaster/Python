# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 21:53
# @Author  : poppies
# @File    : 7.命名参数.py
# @Software: PyCharm

"""
形式参数和缺省参数都是在声明函数的过程中创建的
命名参数是调用函数时使用的
"""


def print_info(name, age, address):
    print(f'name: {name}, age: {age}, address: {address}')


# 命名参数
print_info(age=18, name='安娜', address='长沙')


