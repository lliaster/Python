# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 21:00
# @Author  : 顾安
# @File    : 5.类方法.py


# 类方法: 方法中的第一个参数为cls, 并且类方法只能获取类属性或者其他类方法


class Person:
    gender = '男'

    def __init__(self, name):
        self.name = name

    @classmethod
    def info(cls):
        """
        cls和self的功能没有任何区别, 只是self和cls指向的对象不一样
            self: 实例对象
            cls: 类对象
        """
        print('这是一个类方法:', id(cls))
        print(cls.gender)


person = Person('admin')
print('类对象的地址:', id(Person))
person.info()

"""
1.类方法中的第一个参数cls指向的是类本身(类对象)
2.类方法只能获取到类属性和其他的类方法, 无法操作实例属性和实例方法

实例方法可以获取到类中的所有资源
类方法可以获取到类属性和其他的类方法: @classmethod
静态方法无法获取类中的所有资源, 只能通过传递参数的方式获取参数对象: @staticmethod
"""


