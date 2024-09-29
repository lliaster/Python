# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 20:33
# @Author  : poppies
# @File    : 4.字典数据的删除.py
# @Software: PyCharm


stu_info_data = {
    'name': '安娜',
    'age': 18,
    'gender': '女'
}

# 删除指定键值对
del stu_info_data['gender']
print(stu_info_data)

# 弹出字典中的最后一个键值对
stu_info = stu_info_data.popitem()
print(stu_info)  # 返回的是一个元组, 元组中的元素是key, value

# 弹出指定的value
name = stu_info_data.pop('name')
print(name)
print(stu_info_data)

# 清空字典
stu_info_data.clear()
print(stu_info_data)  # 清空了字典内部的元素而已, 字典本身还是存在的

int_list = [1, 2, 3]
int_list.clear()
print(int_list)
