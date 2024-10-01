# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 21:45
# @Author  : poppies
# @File    : 9.深拷贝.py
# @Software: PyCharm

from copy import deepcopy

name_list = [['张三', '李四'], '王五', '赵六', '钱七']

new_name_list = name_list.copy()
print(f'浅拷贝的可变对象地址(new_name_list): {id(new_name_list[0])}')
print(f'浅拷贝的可变对象地址(name_list): {id(name_list[0])}')

print('-' * 30)

new_name_list = deepcopy(name_list)
print(f'深拷贝的可变对象地址(new_name_list): {id(new_name_list[0])}')
print(f'深拷贝的可变对象地址(name_list): {id(name_list[0])}')

new_name_list[0][0] = '安娜'
print(f'new_name_list = {new_name_list}')
print(f'name_list = {name_list}')
