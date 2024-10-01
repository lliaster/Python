# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 21:25
# @Author  : poppies
# @File    : 8.浅拷贝.py
# @Software: PyCharm


name_list = [['张三', '李四'], '王五', '赵六', '钱七']

# new_name_list = name_list
#
# print(f'name_list: {id(name_list)}')
# print(f'new_name_list: {id(new_name_list)}')
#
# name_list[0][0] = '安娜'
# name_list[1] = '双双'
# print(f'name_list: {name_list}')
# print(f'new_name_list: {new_name_list}')


# 将原有的数据进行备份
new_name_list = name_list.copy()  # 浅拷贝
new_name_list[1] = '双双'
print(f'new_name_list: {new_name_list}')
print(f'name_list: {name_list}')

"""
所谓的浅拷贝只能拷贝到浅层次的数据
    不可变对象的数据可以被拷贝, 无法拷贝可变对象
    如果浅拷贝了一个嵌套列表, 修改内层列表中的值会对原有列表造成影响
"""

print(f'new_name_list: {id(new_name_list[0])}')
print(f'new_name_list: {id(name_list[0])}')
print('-' * 30)
print(f'new_name_list: {id(new_name_list[1])}')
print(f'new_name_list: {id(name_list[1])}')


new_name_list[0][0] = '安娜'
print(f'new_name_list: {new_name_list}')
print(f'name_list: {name_list}')




