# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 20:02
# @Author  : 顾安
# @File    : 1.魔术方法概览.py


# __doc__: 输出类中的注释
class Foo:
    """
    这是一个自定义的类
    """

    def eat(self):
        pass


print(Foo.__doc__)


# __del__: 在类即将退出时触发此方法
class Person:
    def __del__(self):  # 以py文件什么时候结束为基准
        print('代码即将退出...')


person = Person()


# __call__: 可以让实例对象像函数一样被调用
class Student:
    def __call__(self, *args, **kwargs):
        print('我被执行了...')


student = Student()
student()


# __dict__: 将对象的属性和方法通过字典的方式输出
class Province:
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')


print(Province.__dict__)  # 输出类对象包含的属性和方法
pro_1 = Province('长沙', 410000)
print(pro_1.__dict__)
pro_2 = Province('北京', 110000)
print(pro_2.__dict__)


# __getitem__、__setitem__、__delitem__
class CRUD:
    def __getitem__(self, item):
        print('__getitem__: ', item)

    def __setitem__(self, key, value):
        print('__setitem__: ', key, value)

    def __delitem__(self, key):
        print('__delitem__: ', key)


crud = CRUD()
result = crud['k1']  # 在实例对象中获取一个名为k1的键值对, 会触发__getitem__

crud['k2'] = '安娜'  # 会触发__setitem__

del crud['k2']


"""
关于__class__用于从实例对象中获取这个类的信息
关于__module__用于获取模块(py文件)名称
"""


