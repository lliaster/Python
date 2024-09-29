# -*- coding: utf-8 -*-
# @Time    : 2024/9/9 21:44
# @Author  : poppies
# @File    : 9.while循环嵌套练习.py
# @Software: PyCharm


# 打印类似九九乘法表的结构
i = 1

while i <= 5:
    j = 1  # 内部循环条件不成立当前变量会被重置为1
    while j <= i:
        print('* ', end=' ')
        j += 1
    print()
    i += 1

