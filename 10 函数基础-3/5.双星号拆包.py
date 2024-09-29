# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:42
# @Author  : poppies
# @File    : 5.双星号拆包.py
# @Software: PyCharm

info = {
    'name': '安娜',
    'age': 18
}


# 字典中的key必须和参数名称保持一致才能完成拆包传参
def work(age, name):
    print(f'name: {name}, age: {age}')


work(**info)
