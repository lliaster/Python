# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 20:37
# @Author  : poppies
# @File    : 4.私有方法.py
# @Software: PyCharm


class Cat:
    def __init__(self, name):
        self.name = name
        self.__age = 1  # 私有属性: 不能在一个类的外部使用

    # 私有方法
    def __info(self):
        print(f'名称: {self.name}, 年龄: {self.__age}')

    # 接口: 其实就是用来操作私有属性或私有方法的
    def run_method(self):
        self.__info()


cat = Cat('安娜')
cat.run_method()

# 非法操作
cat._Cat__info()
