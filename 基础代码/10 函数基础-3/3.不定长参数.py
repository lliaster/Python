# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:17
# @Author  : poppies
# @File    : 3.不定长参数.py
# @Software: PyCharm


"""
*args: 类型为元组的不定长参数
**kwargs: 类型为字典的不定长参数
"""


def func_1(*args):
    # 如果一个参数在打印时参数名前面有*号则代表拆包
    # 函数内部返回多个数据一定是元组返回
    print(args)


func_1(1, 2, 3, 4, 5)


# kwargs接收的参数必须是命名参数
def func_2(**kwargs):
    print(kwargs)


func_2(name='admin', sex='男')


def test_attr_1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


test_attr_1(1, 2, 123, 456, 789, name='安娜')


# *args, **kwargs必须在所有类型参数之后, *args必须在**kwargs之前
def test_attr_2(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

