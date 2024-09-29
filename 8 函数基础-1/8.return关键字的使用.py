# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 21:29
# @Author  : poppies
# @File    : 8.return关键字的使用.py
# @Software: PyCharm


def add_num(num_1, num_2):
    print('函数被执行...')
    return num_1 + num_2  # python解释器遇到return除了可以将数据返回出去之外还可以中断函数的执行
    print('函数执行结束...')
    return num_1 - num_2


result = add_num(10, 20)
print(result)


"""
1.执行函数内部代码遇到return会结束当前函数的执行
2.如果函数中有两个return则返回第一个return的结果, 第二个return永远不会被执行
"""
