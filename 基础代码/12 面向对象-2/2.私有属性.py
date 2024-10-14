# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 20:19
# @Author  : poppies
# @File    : 2.私有属性.py
# @Software: PyCharm


class Cat:
    def __init__(self, name):
        self.name = name
        self.__age = 1  # 私有属性: 不能在一个类的外部使用

    def info(self):
        print(f'名称: {self.name}, 年龄: {self.__age}')

    # 操作私有属性必须在一个类的内部完成
    def set_attr(self, age):
        if 1 <= age <= 10:
            self.__age = age
            print('设置成功...')
        else:
            print('参数不合法...')


cat_1 = Cat('小黑')
cat_1.name = '小蓝'
# cat_1.__age = 4  在类的外部直接操作私有属性是不允许的
cat_1.set_attr(4)
cat_1.info()

cat_2 = Cat('小白')
cat_2.info()
