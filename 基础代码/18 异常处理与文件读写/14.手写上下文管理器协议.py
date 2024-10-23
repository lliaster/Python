# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 22:00
# @Author  : 顾安
# @File    : 14.手写上下文管理器协议

"""
上下文管理器是一个协议, 本质上其实是运行了python的内部魔法函数完成的释放功能
"""


class MyOpenFile:
    def __init__(self, file_path):
        self.file_obj = None
        self.file_path = file_path

    # 当开启上下文管理会触发当前函数
    def __enter__(self):
        print('上下文管理被开启...')
        self.file_obj = open(self.file_path)
        return self

    def my_read(self):
        print(self.file_obj.read())

    # 当上下文管理器即将退出时被触发
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        print('上下文管理即将关闭...')


with MyOpenFile('./测试文件.txt') as my_open_file:
    my_open_file.my_read()

"""
__enter__: 当使用with语法时会被触发运行
__exit__: 当with语句执行到最后即将退出时会被触发执行
"""
