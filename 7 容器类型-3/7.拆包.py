# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 21:12
# @Author  : poppies
# @File    : 7.拆包.py
# @Software: PyCharm


nums = [1, 2, 3, 4]
# num_1 = nums[0]
# num_2 = nums[1]
# num_3 = nums[2]
# num_4 = nums[3]
#
# print(num_1, num_2, num_3, num_4)

"""
1.变量位置需要和列表中的元素位置保持一致
2.变量个数与列表中的元素个数保持一致
"""
num_1, num_2, num_4, num_3 = nums
print(num_1, num_2, num_3, num_4)

# 集合拆包无法保证元素的位置赋值
int_set = {item for item in range(1, 5)}
num_1, num_2, num_3, num_4 = int_set
print(num_1, num_2, num_3, num_4)  # pycharm是顺序打印的, 但是不代表集合可以顺序拆包


# 可以使用拆包完成数据的位置互换
a = 1
b = 2

a, b = b, a
print(a, b)

