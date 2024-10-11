# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 21:32
# @Author  : poppies
# @File    : 10.继承练习.py
# @Software: PyCharm


class Animal:
    def eat(self):
        print('正在进食...')

    def drink(self):
        print('正在喝水...')


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{self.name}, {self.age}')


class Cat(Animal):
    pass


dog = Dog('来福', 3)
cat = Cat()


"""
子类本身有方法则不会查询父类！！！

1.如果父类实例化并执行info会报错, 因为当前实例没有对应属性
2.如果多个子类继承了同一个父类则所有子类都具有具有父类中的资源

3.如果要对类本身的功能进行拓展则不要在父类中操作, 拓展功能需要在子类中拓展, 在父类中拓展功能会影响到所有子类
    在定义父类后格式代码要固定, 不要频繁修改
"""

"""
1.了解私有属性、私有方法与对象关联
2.必须熟练使用单继承以及继承查询方式: 向上查询
    自己定义生活场景完成单继承: 父类和子类具有相同的一个方法名称
        子类本身具有的方法
        父类本身具有的方法
"""
