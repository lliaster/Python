# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 20:43
# @Author  : 顾安
# @File    : 5.自定义迭代器


"""
如果想要获取一个迭代器对象那么必须先要创建一个迭代对象
"""


from collections.abc import Iterable, Iterator


class SystemStudent:
    # __iter__方法: 让实例对象支持迭代
    # __iter__方法规定要返回一个对象而不是__next__方法本身
    def __iter__(self):
        return self

    # __next__方法: 让实例对象定义具体的迭代规则
    def __next__(self):
        pass


system_student = SystemStudent()
print(f'是否是迭代对象: {isinstance(system_student, Iterable)}')

print(f'是否是迭代器对象: {isinstance(system_student, Iterator)}')


"""
1.如果在一个类的内部实现了__iter__则这个类的实例对象支持迭代
2.如果在一个类的内部实现了__next__则这个类的实例对象可以获取一个迭代器对象,  __iter__必须要返回这个类的实例自身(self)
"""
