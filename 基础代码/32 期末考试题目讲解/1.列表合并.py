# -*- coding: utf-8 -*-
# @Time    : 2024/11/20 20:02
# @Author  : 顾安
# @File    : 1.列表合并.py


a = [
    'a,1',
    'b,3,22',
    'c,3,4'
]

b = [
    'a,2',
    'b,1',
    'd,2'
]


result_dict = dict()

for item in a + b:
    parts = item.split(',')
    key = parts[0]
    if key not in result_dict:
        result_dict[key] = item
    else:
        value = result_dict[key].split(',')[1:]
        new_value = parts[1:]
        result_dict[key] = key + ',' + ','.join(value + new_value)

print(list(result_dict.values()))



