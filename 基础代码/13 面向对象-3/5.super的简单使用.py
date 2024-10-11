# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 20:51
# @Author  : poppies
# @File    : 5.super的简单使用.py
# @Software: PyCharm

"""
super是python中的一个内置函数
    作用: 可以动态查询到子类的父类实例对象的地址
"""


class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attr(self):
        print(f'姓名: {self.name}, 年龄: {self.age}')


# 子类的构造方法比父类的构造方法多一个属性
"""
如果父类中存在__init__方法并且子类也存在则必须在子类的构造方法中运行父类的构造方法之后才能创建子类的实例属性
"""


class Son(Father):
    def __init__(self, name, age, collage):
        # Father.__init__(self, name, age)  # 硬编码

        super().__init__(name, age)  # 可以根据所在的子类查询对应的父类

        # self.name = name
        # self.age = age
        self.collage = collage


son = Son('安娜', 18, '大专')
son.print_attr()
