# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 20:43
# @Author  : 顾安
# @File    : 6.使用闭包的注意事项


def counter(number):
    def inner():
        # 在内部函数中修改外部函数的参数值
        # number参数的所有权是属于counter函数的不是inner函数
        # inner函数只有获取number参数值的权限, 没有修改权限

        nonlocal number
        # 如果需要在一个函数中修改外层函数的参数值不要用global而是nonlocal
        number += 1
        print(number)

    return inner


func_inner = counter(10)
func_inner()

"""
global: 在一个函数或者一个类的内部修改全局变量需要使用global
nonlocal: 在内部函数中修改外部函数的引用需要使用nonlocal
"""
