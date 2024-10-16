# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 20:34
# @Author  : 顾安
# @File    : 2.单例模式.py


class Singleton:
    _instance = None

    def __init__(self):
        print('init方法被执行...')

    # __new__方法用于创建实例对象
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print('我被触发了 - 1')
            cls._instance = super().__new__(cls, *args, **kwargs)
        print('我被触发了 - 2')
        return cls._instance


s1 = Singleton()
s2 = Singleton()


print(id(s1) == id(s2))


"""
__new__方法是用于创建实例对象用的
__init__方法是用于在已有的实例对象中创建对应的实例属性

__new__方法一定在__init__方法之前执行
"""

