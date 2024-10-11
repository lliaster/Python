# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 21:20
# @Author  : poppies
# @File    : 9.单继承.py
# @Software: PyCharm


class Animal:
    def eat(self):
        print('正在进食...')

    def drink(self):
        print('正在喝水...')

    def __run(self):
        print('正在奔跑...')

    def run_method(self):
        self.__run()

    def info(self):
        print('这是父类中的info方法...')


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'名称: {self.name}, 年龄: {self.age}')


dog = Dog('来福', 5)
dog.info()


dog.eat()
dog.drink()
dog.run_method()  # 可以运行父类中私有方法接口

# 如果要运行父类中的私有属性则需要加上父类名称
dog._Animal__run()


"""
子类在调用父类方法时遵循`向上查询`的查询规则
    如果实例对象调用的方法在类中不存在则会向上查询, 如果类本身存在则不会查询父类
"""


