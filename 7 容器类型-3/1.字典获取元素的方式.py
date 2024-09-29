# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 20:12
# @Author  : poppies
# @File    : 1.字典获取元素的方式.py
# @Software: PyCharm


# 获取字典中的key
stu_info = {
    'user': 'admin',
    'password': '123456'
}

for key in stu_info:
    print(key)


keys = stu_info.keys()  # dict_keys对象, 支持迭代, 类似列表的行为
print(list(keys))  # 可以将dict_keys对象转为列表对象


# 获取字典中的value
print(stu_info.values())  # dict_values对象, 支持迭代, 类似列表的行为
print(list(stu_info.values()))

# 获取字典中所有的key和value
print(stu_info.items())  # dict_items对象, 支持迭代, 类似列表的行为
print(list(stu_info.items()))

# 获取每一个key: value
for key, value in stu_info.items():
    print(key, value)







