# -*- coding: utf-8 -*-
# @Time    : 2024/9/4 21:21
# @Author  : poppies
# @File    : 6.标识符与关键字.py
# @Software: PyCharm


"""
1.标识符
    标识符其实是python中创建的一些特殊名称
        变量名称、函数名称、类名称
        可以把标识符理解成一个人的名字，只是一个代号而已

2.关键字
    cpython内置的一些具有特殊含义的单词

在声明标识符时不能与 关键字/内置函数名称 重复
    print
    type

    如果使用内置函数名称作为变量名会导致内置函数的功能失效
"""

# import就是python中的关键字, 作用是导入模块
import keyword

print(keyword.kwlist)  # 当前打印的单词是不能作为标识符去使用的！！！


