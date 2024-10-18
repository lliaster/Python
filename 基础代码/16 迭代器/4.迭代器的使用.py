# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 20:21
# @Author  : 顾安
# @File    : 4.迭代器的使用

from collections.abc import Iterable, Iterator

"""
可迭代对象 vs 迭代器对象
    迭代器对象一定是可迭代对象
    可迭代对象不一定是迭代器对象

    可迭代对象的作用: 让for循环执行的对象, 可迭代对象无法制定迭代规则
    迭代器对象的作用: 让for循环遵守某种规则返回数据
"""

"""
Iterable: 可迭代对象
Iterator: 迭代器对象
"""

int_list = [item for item in range(1, 4)]
print('是否是迭代对象:', isinstance(int_list, Iterable))
print('是否是迭代器对象:', isinstance(int_list, Iterator))


# 如何创建一个迭代器对象
# iter: 内置函数, 可以返回一个迭代器对象
iter_obj = iter(int_list)
print('是否是迭代器对象:', isinstance(iter_obj, Iterator))

# 如果期望让一个对象转为迭代器对象, 那么这个对象本身必须是可迭代对象
# number = 100
# iter_obj = iter(number)


# 如何使用迭代器
# next是python的内置函数, 可以获取一个迭代器内部的元素
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))  # 第三次调用后应该取值到这个列表的最后一个元素

# print(next(iter_obj))  # 如果列表的元素取到了最后, 再次调用会抛出异常: StopIteration


# 利用迭代器中的next循环取值
# 以下代码本质是for循环的底层执行原理
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        break

# for item in int_list:
#     pass
# for item in iter(int_list):
#     pass


"""
1.迭代对象不一定是迭代器
2.迭代器可以使用python内置的函数iter()进行返回
3.迭代器对象可以使用next()方法获取元素: 运行一次next()返回一个元素
4.如果使用死循环的方式不停的调用next方法就可以获取到一个迭代器对象中的所有元素
5.如果取到最后一个元素并继续执行next()方法会产生异常:StopIteration
6.可以使用之后学习的异常捕获消除报错信息并中断死循环
"""

