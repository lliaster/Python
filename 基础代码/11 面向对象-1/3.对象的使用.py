# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 20:53
# @Author  : poppies
# @File    : 3.对象的使用.py
# @Software: PyCharm

"""
一个类可以创建多个对象, 并且对象与对象之间默认是相互隔离的
不同的对象传递的属性一般都是不一样的
"""


class Dog:
    def __init__(self, dog_name, dog_type):
        print('实例化过程会被触发...')
        self.dog_name = dog_name
        self.dog_type = dog_type

    def print_dog_info(self):
        # self参数可以帮我们找到类中定义的属性
        print(f'名称: {self.dog_name}, 品种: {self.dog_type}')


# 创建多个对象
dog_1 = Dog('旺财', '阿拉斯加')
dog_2 = Dog('安娜', '泰迪')

# 验证两个对象的内存地址和验证类的地址
# print('类的地址:', id(Dog))
# print('对象1的地址:', id(dog_1))
# print('对象2的地址:', id(dog_2))

print(dog_1.dog_name)
print(dog_2.dog_name)


# 对象调用方法和属性
dog_1.print_dog_info()

"""
1.一个类可以创建多个对象, 并且对象与对象之间的地址是隔离的
2.对象可以使用符号 . 查询类中的属性和方法并使用


大家在类的内部所看到的__init__方法无需使用对象调用, 在类的初始化操作时会被自动触发
"""
