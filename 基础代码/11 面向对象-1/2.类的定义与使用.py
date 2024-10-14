# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 20:26
# @Author  : poppies
# @File    : 2.类的定义与使用.py
# @Software: PyCharm


"""
class 类名:
    # 编写的类的属性和方法(函数)
    def run(self):
        # 你要执行的逻辑代码...
"""


class Dog:
    # 构造方法: 可以使用这个方法定义一个类的属性
    def __init__(self, dog_name, dog_type):
        self.dog_name = dog_name
        self.dog_type = dog_type

    # 打印狗的品种的方法
    def print_dog_info(self):
        print(f'名称: {self.dog_name}, 品种: {self.dog_type}')


# 类的实例化: 可以让类返回一个对象
dog_1 = Dog('小黑', '哈士奇')

# 对象的作用: 可以调用一个类的内部方法
dog_1.print_dog_info()

dog_2 = Dog('小白', '萨摩耶')
dog_2.print_dog_info()

# 使用对象打印类中的属性
print(dog_1.dog_name)
print(dog_1.dog_type)

"""
总结:
    1.什么是类: 将特征和行为汇总成一个集合的形式被称之为类
    
    2.如何定义类: 
        需要在类的内部定义属性和方法, 一般属性的定义会使用到特殊的方法: __init__ 
        方法定义直接在类的内部定义函数即可, 函数中的第一个参数必须为self
        
    3.如何使用类: 
        需要对类完成实例化: 类名(补上__init__方法中定义的参数的实体参数)
        实例化完成之后会得到一个对象, 这个对象可以运行类中的方法和操作类中的属性
"""
