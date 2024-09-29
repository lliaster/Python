# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 20:05
# @Author  : poppies
# @File    : 2.for循环的简单使用.py
# @Software: PyCharm


"""
for循环与while循环都能完成对于代码的重复执行的功能

    while循环一般情况下需要单独创建一个计数器用于循环终止
    for循环不需要使用计数器变量

    for循环一般使用在容器类型的迭代环境下
        列表、字典、元组、集合统称为容器类型
"""

"""
for 临时变量 in 可以被迭代的对象:
    你想要执行的代码
"""

# 创建一个测试容器类型用于循环: 列表
# int_list = [1, 2, 3, 4, 5]
# for item in int_list:
#     print(item, end=' ')


# 打印五次自己定义的数据
for i in range(5):
    print('双双胖三斤...')


"""
print
input
type: 判断数据类型
range: 用于生成序列的内置函数(方法)
"""
