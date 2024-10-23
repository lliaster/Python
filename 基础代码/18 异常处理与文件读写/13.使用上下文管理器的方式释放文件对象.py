# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 21:58
# @Author  : 顾安
# @File    : 13.使用上下文管理器的方式释放文件对象


file_path = './测试文件.txt'

# 使用with创建上下文管理则无需手动调用close
with open(file_path, encoding='utf-8') as file_obj:
    print(file_obj.read())
