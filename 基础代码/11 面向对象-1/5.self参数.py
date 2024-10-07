# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 21:25
# @Author  : poppies
# @File    : 5.self参数.py
# @Software: PyCharm


class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        # 默认情况下self参数接收的是这个类的对象本身
        # self是哪个对象调用的那么self就是这个对象
        print(self)
        print(self.name)


p1 = Person('安娜')
p1.info()
print(p1)

p2 = Person('安娜')
p2.info()
print(p2)


# self本质上其实就是一个普通的参数而已, 如果使用的是对象调用的方式则把这个对象传递进去
# 如果使用的是类的方式运行的方法, 则可以自己传递一个值
p3 = Person('双双')

# 通过类的方式运行的方法
Person.info(p3)


# 探究使用对象的方式执行类中的方法self是如何接收值的
# 对象去运行一个类的方法需要从类中找到这个方法
print(id(p3.__class__))
print(id(Person))

# 如果你是使用了p3.info()等同于运行了下方的代码
# p.info() == p.__class__.info(p)
p3.__class__.info(p3)




