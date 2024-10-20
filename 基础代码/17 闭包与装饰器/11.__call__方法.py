# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 21:56
# @Author  : 顾安
# @File    : 11.__call__方法


"""
__call__方法可以让一个类的实例像函数一样被调用
"""


class Person:
    def __call__(self, *args, **kwargs):
        print('我被执行了...')


# person = Person()
# person()

Person()()
