# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 20:22
# @Author  : poppies
# @File    : 2.获取字典中指定的value.py
# @Software: PyCharm


# 如果需要获取字典中指定的value值, 建议使用dict对象中内置的get方法
person = {
    'name': '安娜',
    'age': 18,
    'gender': '女'
}

print(person['gender'])  # 如果key不存在则会报错
# print(person['address'])

print(person.get('address'))  # 如果使用get方法获取一个不存在的key则返回一个空值
print(person.get('address', '当前数据不存在'))  # 自定义key不存在的信息

"""
如果根据key获取value, 当key不存在会引发报错, 通过get方法解决当前问题
    如果key不存在则get返回了一个默认值: None
    这个默认值可以自己自定义
"""
