 # -*- coding: utf-8 -*-
# @Time    : 2024/10/11 20:44
# @Author  : 顾安
# @File    : 4.静态方法.py

"""
在创建类的过程中定义方法有以下几个类型:
    实例方法: 方法中的第一个参数为self则是实例方法
    静态方法: 方法中的第一个参数不做限制, 并且静态方法无法获取类中的资源(属性和其他方法)
"""


class Person:
    gender = '男'

    def __init__(self, name):
        self.name = name

    # 定义静态方法
    @staticmethod
    def info():
        # 静态方法无法获取和使用属性与其他方法的
        print('这是一个静态方法...')

    def self_info(self):
        print('这是一个实例方法...')
        print(self.name, self.gender)


person = Person('admin')
person.self_info()

# 调用静态方法: 支持通过实例对象和类对象的方式调用
person.info()
Person.info()

"""
静态方法能实现的功能在实例方法中都能实现
    静态方法相对于实例方法占用的内存更小
    
    * 静态方法无法访问到类中的属性和调用其他的方法
    静态方法其实就是一个具有访问权限的函数而已
"""
