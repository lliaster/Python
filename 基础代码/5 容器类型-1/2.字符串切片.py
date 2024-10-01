# -*- coding: utf-8 -*-
# @Time    : 2024/9/13 20:09
# @Author  : poppies
# @File    : 2.字符串切片.py
# @Software: PyCharm


str_data = 'abcdef'
print(str_data[1])


# 使用切片的方式获取字符串中的部分数据
"""
str_data[起始位置(如果不写默认为0):结束位置:步长(如果不写默认为1)]
"""
print(str_data[1:3])  # 如果需要取到字母c那么就需要获取到这个字母的下标并 + 1
print(str_data[:3])
print(str_data[2:5])
print(str_data[:4:2])

# -1可以获取到这个字符串中最后一个元素的前一个元素
print(str_data[1:-1])
print(str_data[1:])  # 获取到最后一个元素

# 步长为负数的情况
# 取值方向是从右到左
print('步长为负数的情况:', str_data[4:1:-1])

# 获取字符串中的左右字母
print(str_data[:])
print(str_data[::])

# 如果需要将字符串倒序输出则设置步长为负数即可
print(str_data[::-2])
print(str_data[::-1])









