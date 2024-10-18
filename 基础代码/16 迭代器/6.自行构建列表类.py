# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 20:53
# @Author  : 顾安
# @File    : 6.自行构建列表类


class MyList:
    def __init__(self):
        # 列表索引
        self.index = 0
        self.items = list()

    def __iter__(self):
        return self

    def __next__(self):
        # 定义元素返回的迭代逻辑
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            self.index = 0
            raise StopIteration  # 手动抛出异常

    def add_number(self, item):
        self.items.append(item)


my_list = MyList()
my_list.add_number(1)
my_list.add_number(2)
my_list.add_number(3)

new_list = list()
new_list.extend(my_list)
print(new_list)

