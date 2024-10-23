# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 20:32
# @Author  : 顾安
# @File    : 4.try语句的使用


def work(a, b):
    result = a / b
    print(result)


# work(9, 3)

try:
    work(9, 0)
except ZeroDivisionError as e:
    print('程序执行异常:', e)

# try:
#     work(9, 0)
# except Exception as e:
#     print('程序报错了:', e)


"""
Exception: 是python内置的一个异常父类, 所有的异常子类全部继承Exception
    我们在编辑代码时如果能确定一段代码的报错信息, 则尽量不要用Exception
    
ZeroDivisionError: python内置的异常子类
"""
