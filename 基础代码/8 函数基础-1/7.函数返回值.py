# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 21:20
# @Author  : poppies
# @File    : 7.函数返回值.py
# @Software: PyCharm


"""
一个函数在执行完逻辑代码后一般会有最终结果, 如果想要获取到这个最终结果并赋值给一个变量
则需要用到返回值操作

返回值需要用到python中的关键字: return
"""


def add_num(num_1, num_2):
    # 可以将计算结果返回出去并赋值给一个变量
    return num_1 + num_2


# num_1是第一个函数的结果
def sub_num(num_1, num_2):
    return num_1 - num_2


result = add_num(9, 2)
result = sub_num(result, 10)
print(result)


"""
如果第二个函数在计算的过程中需要获取第一个函数的最终结果完成计算
    那么就可以通过return返回最终结果并将结果传递给第二个函数
"""

