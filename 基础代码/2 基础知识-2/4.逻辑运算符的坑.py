# -*- coding: utf-8 -*-
# @Time    : 2024/9/6 21:37
# @Author  : poppies
# @File    : 4.逻辑运算符的坑.py
# @Software: PyCharm

# and左右两边的常量如果都为真则返回右边的值
# and左边的值为假则直接返回左边的值
# and左边的值为真右边为假则返回右边的
print(100 and 200)
print(0 and 100)
print(100 and 0)


print(100 and 100 > 50)


# or 也是一样的
print(100 or 200)





