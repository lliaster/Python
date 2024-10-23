# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 20:01
# @Author  : 顾安
# @File    : 1.内容回顾 - 带有自身参数的类装饰器


# class Loging:
#     def __init__(self, func_obj):
#         self.func_obj = func_obj
#
#     def __call__(self, *args, **kwargs):
#         print(f'被调用的函数名称为: {self.func_obj.__name__}')
#         self.func_obj(*args, **kwargs)
#
#
# @Loging
# def send_message(name, content):
#     print(f'{name}: {content}')
#
#
# send_message('安娜', '你好')

class Loging:
    def __init__(self, level):
        self.level = level

    def __call__(self, func_obj):
        def wrapper(*args, **kwargs):
            print(f'[{self.level}]被调用的函数名称为: {func_obj.__name__}')
            func_obj(*args, **kwargs)

        return wrapper


@Loging('info')
def send_message(name, content):
    print(f'{name}: {content}')


send_message('安娜', '你好')

# loging = Loging(send_message, 'info')
# loging('安娜', '你好')


# loging = Loging('info')
# wrapper = loging(send_message)
# wrapper('安娜', '你好')


"""
1.如果类装饰器自身携带参数则需要在构造方法中将自身需要的参数传递进去
2.使用__call__方法接收被装饰的函数的引用
3.在__call__方法内部实现一个函数, 如果被装饰的函数有参数则内部的装饰函数使用不定长参数进行接收
4.在内部装饰函数中运行被装饰的函数
5.在__call__方法中返回内部装饰函数的引用
"""
