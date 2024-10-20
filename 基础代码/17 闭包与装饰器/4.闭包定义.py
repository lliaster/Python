# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 20:32
# @Author  : 顾安
# @File    : 4.闭包定义


def func_1():
    def func_2():
        print('这是内部函数...')

    # func_1的返回值是内部func_2函数的内存引用
    return func_2


func_2_obj = func_1()
func_2_obj()


def person(name):
    def send_message(content):
        print(f'{name}: {content}')
    return send_message


"""
闭包一般都是函数嵌套, 并且外层函数返回的结果是内存函数的地址引用
内部函数可以使用外部函数的参数
"""

send_func = person('安娜')
send_func('今晚我家没人...')
