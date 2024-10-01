# -*- coding: utf-8 -*-
# @Time    : 2024/9/9 20:24
# @Author  : poppies
# @File    : 3.else的使用.py
# @Software: PyCharm


local_name = 'admin'
local_password = '123456'

username = input('请输入用户名: ')
password = input('请输入密码: ')  # 输入的密码的类型是字符串类型

if username == local_name and local_password == password:
    print('登录成功...')
else:  # 如果条件不成立则执行else之下的代码
    print('登录失败...')

"""
if 条件:
    条件成立时会被执行的代码...
else:
    条件不成立时会被执行的代码...
"""
