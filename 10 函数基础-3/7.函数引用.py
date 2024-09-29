# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:54
# @Author  : poppies
# @File    : 7.函数引用.py
# @Software: PyCharm


# 如何获取一个函数的内存地址
def solution():
    print('这是一个测试函数')


print(id(solution))

work = solution
print(id(work))

work()


# 函数地址引用是可以传递的

