# -*- coding: utf-8 -*-
# @Time     : 2024/10/24 16:37
# @Author   : Lliaster
# @File     : 表格类.py

import time

class Loging:
    def __init__(self, level):
        self.level = level

    def __call__(self, func_obj):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print(f'[{self.level}]被调用的函数名称为: {func_obj.__name__}')
            func_obj(*args, **kwargs)
            end_time = start_time
            print('耗时:', end_time - start_time)
        return wrapper

#
# class Table:
#     def __init__(self, table):
#         self.table = table
#
#     def get_row(self,table,row):
#         if row < len(table):
#             return table[row]
#
#     def get_col(self,table,col):
#         if col< len(table[0]):
#             return [row[col] for row in table]
#
#
# table1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# table = Table(table1)
# print(table.get_row(table1,3))



class Table:
    def __init__(self, table, col_num = 0):
        self.table = table
        self.col_num = col_num

    def ins_list(self,list):
        self.table.append(list)

    def len_table_row(self):
        return len(self.table)

    def len_table_col(self,col_num=10):
        col_num+=3
        print('被调用次数',self.col_num,col_num)
        col_num+=2
        if self.col_num > 1:
            return self.table.len_table_col()
        else:
            self.col_num+=1
        if len(self.table) == 0:
            return 0
        return len(self.table[0])

table = Table([])
print(table.table)
print(table.len_table_col())
print(table.len_table_col())
# print(table.len_table_row())
# print(table.len_table_row())