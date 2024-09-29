# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:46
# @Author  : poppies
# @File    : 6.拆包测试.py
# @Software: PyCharm


info = {
    'name': '安娜',
    'age': 18
}


# 字典中的key必须和参数名称保持一致才能完成拆包传参
def work(*args, **kwargs):
    print(f'args: {args}, kwargs: {kwargs}')
    print(kwargs.get('name'), kwargs.get('age'))
    print(kwargs.values())


work(*info, **info)


"""
如果使用*号获取字典中的数据则只能返回字典中的key
如果使用**号获取字典中的数据则返回包含key和value的数据
"""

