# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 21:59
# @Author  : 顾安
# @File    : 12.基于类的装饰器


class Loging:
    def __init__(self, func_obj):
        self.func_obj = func_obj

    def __call__(self, *args, **kwargs):
        print(f'被装饰的函数名称为: {self.func_obj.__name__}')
        print(f'args={args}, kwargs={kwargs}')
        self.func_obj(*args, **kwargs)


# @Loging
def send_message(name, content):
    print(f'{name}: {content}')


# send_message('安娜', '今晚我家没人...')


# 使用旧语法实现
loging = Loging(send_message)
loging('安娜', '今晚我家没人...')  # 实例对象加括号会触发__call__方法, 并且可以给__call__传递参数
