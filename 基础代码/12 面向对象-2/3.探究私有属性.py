# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 20:31
# @Author  : poppies
# @File    : 3.探究私有属性.py
# @Software: PyCharm


class Cat:
    def __init__(self, name):
        self.name = name
        self.__age = 1  # 私有属性: 不能在一个类的外部使用


# 1.获取私有属性的值
cat = Cat('小黑')
# print(cat.__age)  在一个类的外部无法查询私有属性

# 2.使用 _类名.__属性名获取私有属性
# 通过代码发现cpython解释器在执行私有属性的过程中完成二次命名
print(cat._Cat__age)

# 3.使用以上方式修改私有属性的值
cat._Cat__age = 4
print(cat._Cat__age)

"""
以上代码只是探究私有属性在cpython解释器内部的操作, 不要在项目代码中使用
    私有属性设置的目的是保护数据
"""
