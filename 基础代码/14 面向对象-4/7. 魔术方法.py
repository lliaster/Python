# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 21:24
# @Author  : 顾安
# @File    : 7. 魔术方法.py


"""
__init__
__str__
__repr__
__del__

__getattribute__
"""


class Person:
    def __init__(self):
        print('这是构造方法, 类实例化时会调用此方法...')

    def __str__(self):
        return '这是自定义的实例对象信息...'

    def __repr__(self):
        return '在交互环境中打印实例对象的自定义信息...'

    def __del__(self):
        print('在类执行即将结束时会调用此方法...')


# person = Person()
# print(person)  # print函数会触发类中的__str__方法


class Student:
    country = '中国'

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.__address = address

    def info(self):
        print(self.name, self.age, self.__address, Student.country)  # 使用类对象获取国家

    def __info_method(self):
        print(self.name, self.age, self.__address, self.country)  # 使用实例对象获取国家

    def __getattribute__(self, item):  # item传入的是属性名而不是属性值
        print('开始校验属性或方法:', item)
        return object.__getattribute__(self, item)  # 返回属性值


stu = Student('安娜', 18, '长沙')

# 打印实例属性
# print(stu.name)

# 打印类属性
# print(stu.country)

# 打印私有属性
# print(stu._Student__address)

# 校验方法
# stu.info()

# 校验私有方法
# stu._Student__info_method()


"""
类对象无法触发__getattribute__方法
"""
# 通过类名打印类属性
print(Student.country)
