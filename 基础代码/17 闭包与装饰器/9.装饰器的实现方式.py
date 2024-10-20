# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 21:18
# @Author  : 顾安
# @File    : 9.装饰器的实现方式


"""
需要对功能代码进行debug并输出日志
"""


def debug(func_obj):
    # print(id(func_obj))

    def wrapper():
        print('被调用的函数名称为:', func_obj.__name__)

    return wrapper


@debug
def work():
    # 打印被调用的函数名称并做日志记录
    # print('被调用的函数为:', work.__name__)
    print('这是一个测试函数...')


# 装饰器调用的旧语法
# wrapper_obj = debug(work)
# wrapper_obj()


# 使用装饰器新语法调用装饰器并输出信息
work()
# 现在运行的work不是work函数而是wrapper函数

"""
@debug 相当于 work = debug(work)
"""
