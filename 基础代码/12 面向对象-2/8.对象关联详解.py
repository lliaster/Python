# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 21:14
# @Author  : poppies
# @File    : 8.对象关联详解.py
# @Software: PyCharm


class ClassRoom:
    def __init__(self, name):
        self.cls_name = name
        self.stu_obj = None


class Student:
    def __init__(self, name):
        self.stu_name = name


cls = ClassRoom("爬虫一班")
stu = Student("安娜")

# 将stu实例赋值给stu_obj属性
cls.stu_obj = stu

print(id(cls.stu_obj))
print(id(stu))

# stu_obj属性保存的是学生类实例本身的地址, 所以可以通过stu_obj查询到学生类实例本身并查询stu_name属性