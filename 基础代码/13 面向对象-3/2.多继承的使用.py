# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 20:30
# @Author  : poppies
# @File    : 2.多继承的使用.py
# @Software: PyCharm


class A:
    def run_a(self):
        print('这是类A中的run方法')

    def run(self):
        print('这是类A中的run方法')


class B:
    def run_b(self):
        print('这是类B中的run方法')

    def run(self):
        print('这是类B中的run方法')


# 类C可以获取不同的父类中的资源
class C(A, B):
    pass


c = C()
c.run_a()
c.run_b()

# 多继承存在继承顺序, A在前就先查询,B在后则后查询
c.run()
