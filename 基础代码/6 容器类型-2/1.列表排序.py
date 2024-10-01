# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 20:01
# @Author  : poppies
# @File    : 1.列表排序.py
# @Software: PyCharm


int_list = [1, 3, 2, 4]
int_list.sort()  # 将列表中的元素从小到大进行排序
print(int_list)

# reverse: 反转
int_list.sort(reverse=True)
print(int_list)

"""
sort方法修改的是原有列表的值
"""
int_list = [1, 3, 2, 4]
int_list.reverse()
print(int_list)


# python的内置函数
new_list = sorted(int_list)  # 返回了一个重新排序的新列表
print(new_list)



