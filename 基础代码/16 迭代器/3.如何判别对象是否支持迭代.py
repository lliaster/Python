# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 20:15
# @Author  : 顾安
# @File    : 3.如何判别对象是否支持迭代


from collections.abc import Iterable

int_list = [1, 2, 3, 4]

info_dict = {
    'username': 'admin',
    'password': 123456
}

number = 100

# isinstance: 判断一个实例对象是否是指定的类(父类)的实例
print(isinstance(int_list, Iterable))  # 判断一个对象是否是一个迭代对象, 如果是则返回True
print(isinstance(info_dict, Iterable))
print(isinstance(number, Iterable))

# isinstance: 参数1(实例对象), 参数2(类对象)




