# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 20:04
# @Author  : poppies
# @File    : 1.面向过程与面向对象的代码对比.py
# @Software: PyCharm


# 通过代码的方式输出学生的信息
def print_student_info(name, gender):
    print(f'学生姓名: {name}, 学生性别: {gender}')


# stu_name = '安娜'
# stu_gender = '女'
# print_student_info(stu_name, stu_gender)

# stu_name = '双双'
# stu_gender = '女'
# print_student_info(stu_name, stu_gender)

# stu_name = '夏洛'
# stu_gender = '男'
# print_student_info(stu_name, stu_gender)


name_list = ['安娜', '双双', '夏洛']
gender_list = ['女', '女', '男']

# for info in zip(name_list, gender_list):
#     print_student_info(*info)


"""
zip可以将两个容器类型压缩成一个元组
    根据两个容器类型中的元素压缩, 元素与元素的位置要一致
"""


class PrintStudentInfo:
    def __init__(self, name, gender):
        self.stu_name = name
        self.stu_gender = gender

    def print_student_info(self):
        print(f'学生姓名: {self.stu_name}, 学生性别: {self.stu_gender}')


stu_1 = PrintStudentInfo('安娜', '女')
stu_2 = PrintStudentInfo('双双', '女')
stu_3 = PrintStudentInfo('夏洛', '男')

stu_1.print_student_info()
stu_2.print_student_info()
stu_3.print_student_info()

stu_1.address = '长沙'
print(stu_1.stu_name, stu_1.stu_gender, stu_1.address)


"""
虽然从代码量的角度上说函数的实现方式更简单
    但是如果期望加上一些学生的新的信息就比较麻烦

所以如果数据是固定的可以直接用函数, 如果需要动态添加新的数据那么更推荐类的方式
"""


