# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 20:08
# @Author  : 顾安
# @File    : 1.多态.py


class Dog:
    def bark(self):
        print('狗汪汪叫...')


class LangDog(Dog):
    def bark(self):
        print('狼狗汪汪叫...')


class ZangAo(Dog):
    pass


class Person:
    def pk_dog(self, dog_obj):
        print('常威在打来福...')
        dog_obj.bark()


anna = Person()
dog_1 = Dog()
dog_2 = LangDog()
dog_3 = ZangAo()

anna.pk_dog(dog_1)
anna.pk_dog(dog_2)
anna.pk_dog(dog_3)


"""
如果子类重写了父类中的方法并调用后返回的结果不一致则为多态
    1.继承
    2.重写
"""
