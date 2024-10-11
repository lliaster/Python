# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 21:02
# @Author  : poppies
# @File    : 6.super在单继承环境中的使用.py
# @Software: PyCharm


class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attr(self):
        print(f'姓名: {self.name}, 年龄: {self.age}')


class Son(Father):
    # 子类创建构造方法必须将父类中的参数补齐
    def __init__(self, name, age, collage):
        super().__init__(name, age)

        self.collage = collage

    def print_attr(self):
        print(f'姓名: {self.name}, 年龄: {self.age}, 学历: {self.collage}')


class GrandSon(Son):
    def __init__(self, name, age, collage, address):
        # Son.__init__(self, name, age, collage)

        super().__init__(name, age, collage)
        self.address = address

    def print_attr(self):
        print(f'姓名: {self.name}, 年龄: {self.age}, 学历: {self.collage}, 地址: {self.address}')


grand_son = GrandSon('安娜', 19, '本科', '南京')
grand_son.print_attr()


"""
如果在子类中需要调用父类中的方法可以采用super的形式运行
    尤其是在子类的构造函数中
"""

# 如何快速查询对象中存在的属性和方法
print(dir(grand_son))
