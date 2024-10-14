# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 21:20
# @Author  : 顾安
# @File    : 6.查询类中的方法与属性.py


class Person:
    name = '安娜'

    def __init__(self):
        self.gender = '女'

    def self_info(self):
        pass

    @staticmethod
    def static_info():
        pass

    @classmethod
    def class_info(cls):
        pass


print('类对象中包含的属性与方法:', dir(Person))

p = Person()
print('实例对象中包含的属性与方法:', dir(p))
