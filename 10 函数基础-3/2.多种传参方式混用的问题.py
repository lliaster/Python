# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:10
# @Author  : poppies
# @File    : 2.多种传参方式混用的问题.py
# @Software: PyCharm


def work(a, b, c=100, d=200):
    print(f'a: {a}, b: {b}, c: {c}, d: {d}')


work(11, 22)
work(11, 22, 33)
work(11, 22, 33, 44)

# 错误的调用方式
# work(c=11, d=22)

# 调用参数时如果存在形式参数和缺省参数, 那么实体参数必须在前, 命名参数在后
# work(c=11, d=22, 33, 44)




