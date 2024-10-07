# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 21:12
# @Author  : poppies
# @File    : 4.实例属性和实例方法.py
# @Software: PyCharm


"""
实例属性: 属性名称之前有self前缀则就是一个实例属性
实例方法: 函数中的第一个参数为self则这个函数就是一个实例方法
"""


class Person:
    # 实例属性一般是通过__init__创建的
    def __init__(self, name, age, gender):
        # self.xxx 就是一个实例属性
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print(self.name, self.age, self.gender)

    # 可以自己定义一个普通的实例方法创建实例属性
    # 但是一般不这么用
    def set_attr(self, id_card, height):
        self.card = id_card
        self.height = height


p1 = Person('安娜', 18, '女')
print(p1.name)
p1.info()

"""
实例属性和实例方法只能被当前这个类的对象所使用
    无法直接使用类直接操作类中的实例属性和实例方法
"""
# print(Person.name)
# print(Person.info())

# 可以使用对象动态添加新的实例属性
p1.address = '长沙'
print(p1.address)

p1.set_attr('34119923xxxx', 276.33)
print(p1.card, p1.height)

"""
实例属性的创建方式:
    1.__init__创建, 是最常用的一种
    2.使用对象创建
    3.定义实例方法创建实例属性, 这种方式不常用
"""
