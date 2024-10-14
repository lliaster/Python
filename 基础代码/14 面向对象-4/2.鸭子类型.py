# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 20:14
# @Author  : 顾安
# @File    : 2.鸭子类型.py


"""
如果一个对象的叫声像鸭子, 走路也像鸭子, 则这个对象就是一只鸭子
如果对象的行为与特征像另外一个对象则可以认为这两个对象是一个类型

面向对象中的属性我们可以理解为特征, 方法可以理解为行为
"""


class Dog_1:
    def sleep(self):
        print('正在睡觉 - 1')


class Dog_2:
    def sleep(self):
        print('正在睡觉 - 2')


class Dog_3:
    def sleep(self):
        print('正在睡觉 - 3')


def run_sleep(*args):
    for item in args:
        item.sleep()


dog_1 = Dog_1()
dog_2 = Dog_2()
dog_3 = Dog_3()

run_sleep(dog_1, dog_2, dog_3)

int_list = [1, 2, 3]
int_list.extend((4, 5, 6))
print(int_list)
int_list.extend({7, 8, 9})
print(int_list)
