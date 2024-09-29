# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 21:41
# @Author  : poppies
# @File    : 11.字典的定义.py
# @Software: PyCharm

# 多个列表中的元素完成元素绑定比较麻烦
# name_list = ['张三', '李四', '王五']
# age_list = [20, 17, 22]


"""
字典 = {
    key: value,
}

键值对需要通过冒号进行分割
一个键值对就是字典的一个元素
元素与元素之间需要通过逗号分割
"""
stu_info_dict = {
    'username': '张三',
    'age': 17
}

print(stu_info_dict['username'], stu_info_dict['age'])
