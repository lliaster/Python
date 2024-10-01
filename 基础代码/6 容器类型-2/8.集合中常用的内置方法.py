# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 21:16
# @Author  : poppies
# @File    : 8.集合中常用的内置方法.py
# @Software: PyCharm


int_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 添加元素
int_set.add(11)
print(int_set)  # 在pycharm中直接打印集合元素是有序的, 但是要记住集合本身一定是无序的

# 删除元素
int_set.remove(10)
print(int_set)

# 批量添加
int_set.update(['1', '2', '3'])
print(int_set)

# 随机弹出一个元素, pop默认返回的是最后一个元素, 但是集合中的元素是无序的, 所以没有办法确定最后一个元素的值
data = int_set.pop()
print(data)

# 集合元素必须是不可变对象/可哈希对象
data_set = {1, '2', 3.14, False, (1, 2, 3)}
print(data_set)

# 可变对象无法作为集合的元素
data_set = {[1, 2, 3], {'name': '安娜'}}
print(data_set)
