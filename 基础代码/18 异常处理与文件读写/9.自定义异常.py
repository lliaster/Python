# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 21:11
# @Author  : 顾安
# @File    : 9.自定义异常


class LoginError(Exception):
    def __str__(self):
        return '用户名或密码错误...'


# 账号登录
def login(username, password):
    local_username = 'admin'
    local_password = '123456'

    try:
        if local_username == username and local_password == password:
            print('登录成功...')
        else:
            raise LoginError
    except Exception as e:
        print('程序异常:', e)


login('admin', 123456)
