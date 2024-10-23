# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 21:17
# @Author  : 顾安
# @File    : 10.文件数据读取

# 1.声明读取的文件的路径（相对路径）
file_path = './测试文件.txt'

# 2.使用open函数打开一个文件并指定编码集
# 如果读取数据出现乱码则使用encoding指定编码读取
file_obj = open(file_path, encoding='utf-8')

# 3.使用返回的对象完成数据的读取, read()方法是从文件开头一直读取到文件结尾
print(file_obj.read())
file_obj.read()

# 4.将每一行的数据作为一个列表的元素读取
# print(file_obj.readlines())

# 5.读取第一行数据
# print(file_obj.readline())
