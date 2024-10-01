# -*- coding: utf-8 -*-
# @Time    : 2024/9/9 21:24
# @Author  : poppies
# @File    : 8.while循环嵌套.py
# @Software: PyCharm


# size = 5
# line = '* ' * size
# count = 0
# while count < size:
#     print(line)
#     count += 1

size = 5
row = 1

while row <= size:
    col = 1
    while col <= size:
        print('*', end=' ')
        col += 1
    print()
    row += 1


# 在一般的开发中, 为了代码的可读性, 基本不会写嵌套代码, 如果有嵌套需求, 也会将嵌套代码进行拆分

