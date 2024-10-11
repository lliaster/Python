# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 21:21
# @Author  : poppies
# @File    : 7.super在多继承环境中的使用.py
# @Software: PyCharm


class Parent:
    def __init__(self, name, *args):
        print('parent的init被调用...')
        self.name = name
        print('parent的init结束调用...')


class Son1(Parent):
    def __init__(self, name, age, *args):
        print('son1的init被调用...')
        # Parent.__init__(self, name)
        super().__init__(name, *args)
        self.age = age
        print('son1的init结束调用...')


class Son2(Parent):
    def __init__(self, name, gender, *args):
        print('son2的init被调用...')
        # Parent.__init__(self, name)

        super().__init__(name, *args)
        self.gender = gender
        print('son2的init结束调用...')


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print('grand_son的init被调用...')
        # Son1.__init__(self, name, age)
        # Son2.__init__(self, name, gender)

        super().__init__(name, age, gender)
        print('grand_son的init结束调用...')


grand_son = GrandSon('安娜', 20, '女')

# super的调度顺序是根据继承链来的
print(GrandSon.__mro__)


"""
1.在多继承环境中不要使用父类名调用构造函数, 在菱形继承中会导致父类的构造方法重复执行
2.super方法调用的顺序参考__mro__返回的继承链顺序
3.在多继承环境中要注意参数的传递位置, 建议使用缺省参数的方式传递
"""
