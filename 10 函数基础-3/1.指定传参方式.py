# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:01
# @Author  : poppies
# @File    : 1.指定传参方式.py
# @Software: PyCharm


# 如果定义函数的过程中存在*参数, 则代表*号后面的参数必须使用缺省参数
def print_info_1(name, age, *, gender, address):
    print(f'name: {name}, age: {age}, gender: {gender}, address: {address}')


# 后面两个参数的传递方式必须是命名参数的传递方式
print_info_1('admin', 18, gender='女', address='长沙')


# 如果定义函数的过程中存在/参数, 则代表/前面的参数必须使用实体参数传递
def print_info_2(name, age, /, gender, address):
    print(f'name: {name}, age: {age}, gender: {gender}, address: {address}')


print_info_2('admin', 18, '女', '长沙')
