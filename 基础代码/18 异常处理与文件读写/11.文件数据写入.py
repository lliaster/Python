# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 21:47
# @Author  : 顾安
# @File    : 11.文件数据写入


"""
文件读写有两种情况:
    1.覆盖写: 将原有的数据清空并写入新数据(mode='w')
    2.追加写: 在原有的数据之后继续写入新数据(mode='a')
"""

file_path = './测试文件.txt'
file_obj = open(file_path, mode='a')
file_obj.write('\n双双胖三斤...')

# file_obj = open(file_path, mode='w')
# file_obj.write('双双胖三斤...')
