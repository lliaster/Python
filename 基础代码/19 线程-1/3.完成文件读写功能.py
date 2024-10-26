# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:10
# @Author  : 顾安
# @File    : 3.完成文件读写功能


# 打开文件以更新模式('r+'允许读写)
filename = '测试文件.txt'

with open(filename, 'r+') as file:
    # 写入内容
    file.write('安娜\n')
    file.write('双双\n')

    # 通过seek方法把文件指针移动到文件的开头
    file.seek(0)

    # 读取并打印文件内容
    content = file.read()
    print(content)
