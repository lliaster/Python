# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 20:46
# @Author  : poppies
# @File    : 6.推导式.py
# @Software: PyCharm


# 要创建一个1 - 100的列表
# int_list = []
# for item in range(1, 101):
#     int_list.append(item)
#
# print(int_list)


# 使用列表推导式
int_list = [item for item in range(1, 101)]
print(int_list)

# 生成一定范围内的偶数序列
int_list = [item for item in range(1, 21) if item % 2 == 0]
print(int_list)

# 生成一定范围内的奇数序列
int_list = [item for item in range(1, 21) if item % 2 != 0]
print(int_list)

int_list = [item for item in range(1, 21, 2)]
print(int_list)


# 推导式支持列表、字典、集合, 不包括元组
int_data = (item for item in range(1, 11))
print(int_data)   # 返回的是一个生成器对象, 不是具体的数据


int_set = {item for item in range(1, 21)}
print(int_set)


# 字典推导式用的不多, 了解即可
int_dict = {item: item * item for item in range(1, 11)}
print(int_dict)


# 如果需要创建复杂的列表嵌套结构, 也可以使用推导式生成, 但是不建议用: numpy
int_list = [[x, y] for x in range(1, 3) for y in range(3)]
print(int_list)


"""
建议不要使用推导式生成嵌套的数据结构
    如果需要创建嵌套的数据结构建议大家手写for循环代码
"""
int_list = list()
for x in range(1, 3):
    for y in range(3):
        int_list.append([x, y])
print(int_list)





