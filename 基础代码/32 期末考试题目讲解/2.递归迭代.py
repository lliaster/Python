# -*- coding: utf-8 -*-
# @Time    : 2024/11/20 20:11
# @Author  : 顾安
# @File    : 2.递归迭代.py


a = [1, 2, [3, 4, ['434', ...]]]


def iter_value(lst):
    for item in lst:
        # 判断迭代出来的元素是否是一个列表类型
        if isinstance(item, list):
            iter_value(item)  # 递归调用
        else:
            print(item)


iter_value(a)
