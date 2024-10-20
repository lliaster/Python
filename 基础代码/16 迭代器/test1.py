# -*- coding: utf-8 -*-
# @Time     : 2024/10/18 21:18
# @Author   : Lliaster
# @File     : test1.py
from collections.abc import Iterable, Iterator

int_list = [0, 0, 1, 2, 3]
num = 100
print(isinstance(int_list, Iterable))
print(isinstance(num, Iterable))
int_list = [item for item in range(1, 4)]
print('是否可迭代对象', isinstance(int_list, Iterable))
print('是否迭代器对象', isinstance(int_list, Iterator))

iter_obj = iter(int_list)
print('是否迭代器对象', isinstance(int_list, Iterator))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
# print(next(iter_obj))


print('x' * 55)


class MyList:
    def __init__(self):
        self.index = 0
        self.items = list()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            items = self.items[self.index]
            self.index += 1
            return items
        else:
            raise StopIteration

    def add_number(self,itme):
        self.items.append(itme)


mylist = MyList()
mylist.add_number(0)
mylist.add_number(1)

new_list = list()
new_list.extend(mylist)
print(new_list)