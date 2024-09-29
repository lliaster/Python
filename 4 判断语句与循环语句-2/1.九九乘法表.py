# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 20:01
# @Author  : poppies
# @File    : 1.九九乘法表.py
# @Software: PyCharm

i = 1

# while i <= 5:
#     j = 1
#     while j <= i:
#         print('x*y=z ', end='')
#         j += 1
#     print()
#     i += 1


while i <= 9:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i*j} ', end='')
        j += 1
    print()
    i += 1
