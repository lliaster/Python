# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 21:54
# @Author  : 顾安
# @File    : 12.文件对象使用完毕之后要释放


file_path = './测试文件.txt'
file_obj = open(file_path)
print(file_obj.read())

# 释放文件对象
file_obj.close()
