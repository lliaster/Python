# -*- coding: utf-8 -*-
# @Time    : 2024/11/20 20:14
# @Author  : 顾安
# @File    : 3.根据列表中元素的长度定义字典.py


lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 32769, 65536, 4294967296]

res = dict()
for num in lst:
    digits = len(str(num))
    if digits not in res:
        res[digits] = [num]
    else:
        res[digits].append(num)


print(res)




