# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:36
# @Author  : poppies
# @File    : 4.星号拆包.py
# @Software: PyCharm


def student_info(stu_id, name, cls_name):
    print(f'stu_id: {stu_id}, name: {name}, cls_name: {cls_name}')


stu_list = [10010, '安娜', '爬虫一班']
# student_info(stu_list[0], stu_list[1], stu_list[2])

# 列表中的元素位置必须和函数位置保持一致
# 当前拆包方式只针对列表、元组
student_info(*stu_list)
