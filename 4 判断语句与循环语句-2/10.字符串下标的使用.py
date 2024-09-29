# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 21:52
# @Author  : poppies
# @File    : 10.字符串下标的使用.py
# @Software: PyCharm


str_data = 'abcdef'

print(str_data[2])
print(str_data[0])  # 字符串下标开始位置为0
print(str_data[5])

print('-' * 30)

print(str_data[-1])
print(str_data[-2])
print(str_data[-6])


"""
字符串的索引取值
    str_data[索引值]
    
如果取值方向是从右到左则可以使用负数
    str_data[-1]是获取这个字符串的最后一个元素
"""


