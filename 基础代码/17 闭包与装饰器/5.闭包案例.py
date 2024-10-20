# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 20:40
# @Author  : 顾安
# @File    : 5.闭包案例


def add(num_1):
    def inner_add(num_2):
        return num_1 + num_2

    return inner_add


func_add = add(10)
print(func_add(20))
