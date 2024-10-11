# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 20:39
# @Author  : poppies
# @File    : 4.重写.py
# @Software: PyCharm


"""
如果子类中存在的方法与父类中的方法同名, 则为重写
"""


class A:
    def print_attr(self):
        print('这是类A中的方法...')


class B(A):
    def print_attr(self):
        print('这是类B中的方法...')


b = B()
b.print_attr()  # 因为子类中已经存在这个方法了, 就没有必要去搜索父类中的同名方法

"""
如果在子类中存在父类的相同名称的方法, 则因为就近原则运行的是子类本身的方法而不是父类
    重写可以更改父类中的方法的执行逻辑
    
重写的特征:
    1.继承
    2.必须要重新编写父类方法
"""
