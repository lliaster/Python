# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 20:06
# @Author  : poppies
# @File    : 2.全局变量与局部变量.py
# @Software: PyCharm

"""
内置命名空间: 在任意py文件中都可以执行内置函数, 内置函数存储在内置命名空间中
全局命名空间: 在本文件中定义的变量可以在本文件中使用, 一般不能跨文件使用
局部命名空间: 某一个变量在某一个函数中创建那么只有这个函数能使用这个变量
"""

# 全局变量
# 在当前文件中的任意代码片段都可以访问到这个变量中的值
num = 10


def work_1():
    print(num)


"""
先从函数内部查询是否存在这个变量
	如果有直接用
	如果没有则查询这个py文件中是否存在这个变量
"""


def work_2():
    num = 5  # 局部变量, 内部的变量只能通过这个函数去使用, work_1无法查询到work_2的变量
    print(num)


work_1()
work_2()

# for item in range(1, 10):
#     int_list = list()
#     int_list.append(item)
#
# print(int_list)
# 不建议在for循环外部访问for循环内部数据
