# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 21:29
# @Author  : poppies
# @File    : 9.集合运算.py
# @Software: PyCharm


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 交集运算
print(set1 & set2)

# 并集运算
print(set1 | set2)

# 差集运算
result = set2 - set1
print(result)
result = set1 - set2
print(result)

# 对称差集运算
result = set1 ^ set2
print(result)




