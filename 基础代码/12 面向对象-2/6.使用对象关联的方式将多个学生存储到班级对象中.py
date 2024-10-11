# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 20:51
# @Author  : poppies
# @File    : 6.使用对象关联的方式将多个学生存储到班级对象中.py
# @Software: PyCharm


class ClassRoom:
    def __init__(self, name):
        self.cls_name = name
        self.stu_list = list()

    def add_student(self, student_info):
        self.stu_list.extend(student_info)


class Student:
    def __init__(self, name):
        self.stu_name = name


cls = ClassRoom("爬虫一班")
stu_1 = Student('安娜')
stu_2 = Student('双双')
stu_3 = Student('百川')

cls.add_student([stu_1, stu_2, stu_3])

for item in cls.stu_list:
    print(item.stu_name)


"""
所谓的对象关联的本质是: 在一个类的内部创建了一个属性, 这个属性保存了另外一个类的实例对象地址
"""