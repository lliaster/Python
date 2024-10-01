# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 21:11
# @Author  : poppies
# @File    : 9.利用函数引用完成闭包功能的代码示例.py
# @Software: PyCharm


def work(func_obj):
    def wrapper():
        print('准备执行函数...')
        func_obj()
        print('测试函数执行完毕...')

    return wrapper


def test_method():
    print('这是一个测试函数')


wra_func = work(test_method)
wra_func()
