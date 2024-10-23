# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 20:52
# @Author  : 顾安
# @File    : 6.手动抛出异常


"""
断言是根据某个条件决定是否要抛出异常信息
手动抛出异常没有条件, 可以直接让原本正确的代码抛出错误
"""


# 账号登录
def login(username, password):
    local_username = 'admin'
    local_password = '123456'

    if local_username == username and local_password == password:
        print('登录成功...')
    else:
        # print('登录失败...')
        # raise: python关键字(手动抛出异常)
        raise NameError


login('admin', 123456)
