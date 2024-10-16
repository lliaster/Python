# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 20:45
# @Author  : 顾安
# @File    : 3.动态绑定 - 属性与方法.py

import types


class Person:
    num = 0

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


p1 = Person("安娜", "20")
p1.sex = '女'
print(p1.name, p1.age, p1.sex)

p2 = Person('双双', '24')
# print(p2.sex)  # p1创建了实例属性sex但是p2不存在

# 创建类属性
Person.sex = '男'
print(p2.sex)
print(p1.sex)  # p1对象已经存在实例属性sex, 所以无需查询类属性


# 自定义函数
def run(self, speed):
    print("%s在移动, 速度是%dkm/h" % (self.name, speed))


# 使用实例对象动态添加实例方法
p1.run = types.MethodType(run, p1)
p1.run(120)


# 定义函数, 且设置为类方法
@classmethod
def test_class(cls):
    print("类方法绑定...")
    print("num=%d" % cls.num)
    cls.num = 100
    print("num=%d" % cls.num)
    print()


# 定义函数, 且设置为静态方法
@staticmethod
def test_static():
    print("静态方法绑定...")


# 给Person类绑定类方法: 直接使用类对象的方式添加类方法
Person.test_class = test_class
p1.test_class()


# 给Person类绑定静态方法: 直接使用类对象的方式添加静态方法
Person.test_static = test_static
p2.test_static()
