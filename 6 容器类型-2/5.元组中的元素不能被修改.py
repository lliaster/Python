# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 20:37
# @Author  : poppies
# @File    : 5.元组中的元素不能被修改.py
# @Software: PyCharm


int_tuple = (1, 2, 3)
# int_tuple[0] = 4  元组中的元素修改时会发生报错


# 与列表类似的方法
# 因为元组中的元素一旦固定则不能修改所以元组中没有列表的添加方法/删除方法
print(int_tuple.index(2))
print(int_tuple.count(3))

# 元组支持切片: 会返回一个新元组并且不会对原有元组产生影响
int_tuple = (1, 2, 3, 4, 5)
new_tuple = int_tuple[:4]  # 切片会返回一个新元组所以需要使用一个变量进行接收
print(new_tuple)

