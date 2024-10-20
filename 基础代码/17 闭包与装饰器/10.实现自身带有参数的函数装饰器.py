# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 21:35
# @Author  : 顾安
# @File    : 10.实现自身带有参数的函数装饰器


"""
需求: 在输出日志信息时包含当前被运行的函数名称以及debug等级
"""


def loging(level):
    def wrapper(func_obj):
        def inner_wrapper(*args):
            print(f'[{level}]: 被检测的函数名称为: {func_obj.__name__}')
            func_obj(*args)  # 运行被装饰的函数

        return inner_wrapper
    return wrapper


@loging('info')
def send_message(name, content):
    print(f'{name}: {content}')


# wrapper = loging('info')
# inner_wrapper = wrapper(send_message)
# inner_wrapper('安娜', '今晚我家没人')

send_message('安娜', '今晚我家没人')

"""
1.运行loging函数并传递loging函数所需的参数, 拿到wrapper函数的引用
2.使用获取到的wrapper函数的引用完成函数调用并传递被装饰的函数引用, 拿到inner_wrapper函数的引用
3.使用获取到的inner_wrapper函数的引用完成函数调用并传递被装饰的函数的参数
4.inner_wrapper被执行时会运行func_obj(被装饰的函数)并将被装饰的函数的所需参数传递过去
"""


