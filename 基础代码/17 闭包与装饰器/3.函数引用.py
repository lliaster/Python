# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 20:29
# @Author  : 顾安
# @File    : 3.函数引用


"""
所谓的函数引用其实就是一个函数在内存中的地址
    并且我们可以将地址信息赋值给一个变量
"""


def work():
    print('这是一个自定义函数...')


func_obj = work
func_obj()


"""
使用函数名称获取这个函数的内存地址并赋值给了一个变量func_obj
    那么func_obj指向的内存其实就是原有函数:work
    使用func_obj()相当于work()
"""
