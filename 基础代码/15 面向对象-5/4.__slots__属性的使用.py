# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 21:10
# @Author  : 顾安
# @File    : 4.__slots__属性的使用.py


class Person:
    # 限制类只能创建name和age属性
    __slots__ = ('name', 'age')


p = Person()
p.name = '双双'
p.age = 18
print(p.name, p.age)

# p.gender = '女'
# print(p.gender)

