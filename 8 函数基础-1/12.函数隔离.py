# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 21:49
# @Author  : poppies
# @File    : 12.函数隔离.py
# @Software: PyCharm


def work_1():
    num = 100
    print('num_1:', id(num))
    return num


def work_2():
    num = 200
    print('num_2:', id(num))
    return num


# 打印函数在内存中的地址
print(id(work_1))
print(id(work_2))

print(work_1())
print(work_2())
