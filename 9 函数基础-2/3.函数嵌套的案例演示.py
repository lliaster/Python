# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 20:31
# @Author  : poppies
# @File    : 3.函数嵌套的案例演示.py
# @Software: PyCharm


"""
使用函数打印虚线, 通过另外一个函数去控制打印虚线的次数
"""


def print_one_line():
    print('-' * 30)


def print_num_line(num):
    i = 0
    while i < num:
        print_one_line()
        i += 1


print_num_line(5)

"""
计算三个数的和, 并且获取这三个数的平均值
"""


def add_num(n1, n2, n3):
    print(f'相加结果为: {n1 + n2 + n3}')
    return n1 + n2 + n3


def avg_num(n1, n2, n3):
    res = add_num(n1, n2, n3)  # 外层函数接收到的参数可以直接传递给内部的嵌套函数
    print(f'平均值为: {res / 3:.2f}')


avg_num(5, 7, 22)

