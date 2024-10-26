# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:01
# @Author  : 顾安
# @File    : 1.内容补充 - 读写行


file_path = './测试文件.txt'
stu_name_list = ['安娜', '\n双双', '\n百川']
file_obj = open(file_path, 'w+')
file_obj.writelines(stu_name_list)
file_obj.close()

file_obj = open(file_path, 'r')
print(file_obj.read())
file_obj.close()
