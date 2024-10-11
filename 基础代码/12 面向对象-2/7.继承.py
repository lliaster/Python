# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 20:58
# @Author  : poppies
# @File    : 7.继承.py
# @Software: PyCharm


"""
如果admin的父亲去世了, admin本身会继承父亲的财产
    映射在编程语言中是类中的资源(方法、属性)也是可以被继承的
"""

"""
继承代码模板:
    class 父类:
        pass
        
    class 子类(父类):
        pass
"""


# 动物类
class Animal:
    def eat(self):
        print('正在进食...')


class Dog(Animal):
    pass


dog = Dog()
dog.eat()


"""
在继承关系中, 子类可以使用父类中的所有资源(不包含私有属性和私有方法)
如果一个类名括号中有其他类名, 则这个类就是子类, 括号里面的类是父类
"""
