# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 20:49
# @Author  : 顾安
# @File    : 7.多个闭包


def counter(number):
    def inner():
        nonlocal number
        number += 1
        print(number)

    return inner


func_1 = counter(10)
func_2 = counter(20)

# print(id(func_1))
# print(id(func_2))


func_2()
func_1()

"""
在多个闭包的情况下, 闭包与闭包是内存隔离的, 返回的内部函数地址是不一样

1.闭包的使用方式与面向对象的实例对象类似
2.函数与函数之间必须有包含关系
3.外层函数必须返回内层函数的引用
4.闭包没有办法直接释放变量
"""


