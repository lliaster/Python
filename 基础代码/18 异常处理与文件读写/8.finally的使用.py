# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 21:00
# @Author  : 顾安
# @File    : 8.finally的使用


"""
finally: 无论程序是否报错都会被执行的代码
"""


def work(a, b):
    result = a / b
    print(result)


try:
    work(9, 0)
except Exception as e:
    print('程序异常:', e)
else:
    print('如果执行的代码段没有异常则执行else代码...')
finally:
    print('无论程序是否报错都会被执行...')
