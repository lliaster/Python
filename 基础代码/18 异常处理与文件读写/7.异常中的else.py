# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 20:57
# @Author  : 顾安
# @File    : 7.异常中的else


def work(a, b):
    result = a / b
    print(result)


try:
    work(9, 3)
except Exception as e:
    print('程序异常:', e)
# 执行程序在没有发生异常的情况则会执行else代码
else:
    print('如果执行的代码段没有异常则执行else代码...')
