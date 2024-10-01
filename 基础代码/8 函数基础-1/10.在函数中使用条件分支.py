# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 21:42
# @Author  : poppies
# @File    : 10.在函数中使用条件分支.py
# @Software: PyCharm


def check_num(num):
    if num == 100:
        return num + 1
    elif num == 200:
        return num + 2
    else:
        return 300


print(check_num(100))
print(check_num(200))
print(check_num(123))


"""
可以利用条件分支返回不同的结果
"""

