# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 21:34
# @Author  : 顾安
# @File    : 2.回顾生成器的执行方式.py


def work():
    yield 'hello world'


gen_obj = work()
print(next(gen_obj))
