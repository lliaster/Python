# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 21:09
# @Author  : poppies
# @File    : 7.集合的定义与集合特征.py
# @Software: PyCharm


"""
1.集合中的元素是无序的
2.集合中的元素必须是唯一的
3.集合中的元素是可以被修改的
"""

nums = {100, 200, 300}
print(type(nums))
print(nums)

for item in nums:
    print(item)

nums = set()
print(nums)

nums = {}  # 空集合不能这样定义, 返回的是一个字典类型
print(nums)
print(type(nums))

# 因为集合是无序的, 所以集合不能使用索引下标, 索引取值和切片都无法使用
# nums = {1, 2, 3, 4, 5}
# print(nums[:5])


# 集合中的元素是唯一的
nums = {1, 1, 2, 2, 3, 3, 4, 4}
print(nums)
