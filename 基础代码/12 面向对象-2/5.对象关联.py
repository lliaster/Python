# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 20:43
# @Author  : poppies
# @File    : 5.对象关联.py
# @Software: PyCharm


"""
1.定义一个班级类, 使用班级类创建一个班级实例
2.定义一个学生类, 使用学生类创建一个多个学生实例

根据班级实例查询在这个班级的学生信息
"""


class ClassRoom:
    def __init__(self, name):
        self.cls_name = name


class Student:
    def __init__(self, name):
        self.stu_name = name


cls = ClassRoom('爬虫一班')
stu = Student('安娜')

# 在班级实例中创建了一个新的属性: stu_obj
cls.stu_obj = stu

# 从班级实例中查询实例属性stu_obj并找到student类的对象地址
print(cls.stu_obj.stu_name)

