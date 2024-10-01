# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 20:27
# @Author  : poppies
# @File    : 4.元组类型.py
# @Software: PyCharm


# 元组的行为和列表类似
# 都支持存储多个不同的类型的值以及迭代
# 元组中的元素是不能被修改的


int_tuple = (1, 2, 3)
print(type(int_tuple))

int_tuple = ()  # 不推荐使用这种方式声明空元组
print(type(int_tuple))
int_tuple = tuple()  # 通过当前这种方式来声明空元组
print(type(int_tuple))

int_tuple = (1,)  # 如果你定义的元组中的元素只有一个, 一定要在这个元素的后面加上逗号
print(type(int_tuple))


int_list = [1]  # 列表中如果只有一个元素, 这个元素后面是不需要加逗号的
print(type(int_list))



