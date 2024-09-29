# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 20:30
# @Author  : poppies
# @File    : 3.字典数据的修改与新增.py
# @Software: PyCharm


stu_info_data = {
    'name': '安娜',
    'age': 18,
    'gender': '女'
}

# 在定义好的字典中添加新的key:value
# 如果key不存在则创建新的键值对
stu_info_data['address'] = '长沙'
print(stu_info_data)


# 如果key存在则覆盖原有的数据
stu_info_data['age'] = 20
print(stu_info_data)
