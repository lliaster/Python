# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 21:35
# @Author  : poppies
# @File    : 12.递归函数.py
# @Software: PyCharm


"""
递归函数本质上其实就是一个死循环, 自己调用自己
自己实现的递归我们一般会创建一个退出递归调用的条件
"""


# def test2.py():
#     print('这是一个测试的递归函数...')
#     test2.py()  # 调用test函数

# test2.py()


# 计算斐波那契数列
# def solution(n):
#     if n <= 1:
#         return n
#
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
#
# print(solution(10))

def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return solution(n - 1) + solution(n - 2)


print(solution(10))


"""
递归函数只是作为了解, 在开发中不建议使用
    递归控制不好容易写成死循环
"""
