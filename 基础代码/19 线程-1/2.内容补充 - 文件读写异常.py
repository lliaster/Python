# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:07
# @Author  : 顾安
# @File    : 2.内容补充 - 文件读写异常


file_path = './测试文件-1.txt'

# 如果使用windows系统的同学需要强制加上encoding='utf-8'
try:
    with open(file_path, encoding='utf-8') as f:
        f.read()
except FileNotFoundError:
    print('文件不存在...')
