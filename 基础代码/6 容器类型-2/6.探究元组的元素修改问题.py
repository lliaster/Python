# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 20:46
# @Author  : poppies
# @File    : 6.探究元组的元素修改问题.py
# @Software: PyCharm


# 如何获取一个变量在内存中的地址
# python中的变量保存的都是常量在内存所占用的内存地址
num = 1

# 可以使用python的内置函数id获取变量所保存的内存地址
print(id(num))

# 元组中的元素不可修改其实表达的意思是不能修改元素中的内存地址
data_tuple = (1, 2, 3, [4, 5])

print(f'在修改之前的元素的内存地址: {id(data_tuple[3])}')

data_tuple[3][0] = '4'
print(f'在修改之后的元素的内存地址: {id(data_tuple[3])}')
print(data_tuple)


# 列表的元素修改不会对列表本身的内存地址发生影响

