# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 20:18
# @Author  : poppies
# @File    : 1.函数的定义以及函数的作用.py
# @Software: PyCharm

"""
def是用于定义函数的

def 函数名称():
    你要执行的代码块...
"""


# 定义一个函数, 让函数分别打印出1 2 3
def print_int_data_1():
    print(1)
    print(2)
    print(3)


def print_int_data_2():
    print(4)
    print(5)
    print(6)


# 调用函数后才能执行函数内部的代码
print_int_data_1()

# 重复执行函数内部代码
print_int_data_1()
print_int_data_1()

"""
函数执行类似开关, 如果调用了函数相当于打开了这个函数的开关, 则函数才能被执行
如果函数定义完成之后并没有调用函数则函数是不会执行的


函数可以让代码重复执行, 并且可以通过导包的方式在其他py文件中执行
"""
