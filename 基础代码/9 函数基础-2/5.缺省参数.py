# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 21:45
# @Author  : poppies
# @File    : 5.缺省参数.py
# @Software: PyCharm


"""
缺省参数其实就是定义参数的过程中创建了默认值
"""


def print_info(name, age=18):
    print(name, age)


print_info('admin')
print_info('安娜', 48)


"""
缺省参数的作用:
    1.可以对参数设置默认值
    2.如果在调用函数的过程中没有传递具体的值则使用默认值
    3.如果在调用函数的过程中传递了新的参数则使用新参数
"""


