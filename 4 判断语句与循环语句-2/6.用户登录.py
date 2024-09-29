# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 21:10
# @Author  : poppies
# @File    : 6.用户登录.py
# @Software: PyCharm


local_username = 'admin'
local_password = '123'


# for item in range(3, 0, -1):
#     print(f'剩余{item}次机会')
#     username = input('请输入用户名:')
#     password = input('请输入密码:')
#
#     if username == local_username and password == local_password:
#         print('登录成功...')
#         break


i = 3
while i > 0:
    print(f'剩余{i}次机会')
    username = input('请输入用户名:')
    password = input('请输入密码:')

    if username == local_username and password == local_password:
        print('登录成功...')
        break
    i -= 1



