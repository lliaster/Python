# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 21:30
# @Author  : poppies
# @File    : 8.用户登录 - 优化版本.py
# @Software: PyCharm


"""
for 临时变量 in range(值):
    执行的代码
else:
    循环停止后执行的代码


i = 值
while i < 值:
    执行的代码
else:
    循环停止后执行的代码
"""

local_username = 'admin'
local_password = '123'


# i = 3
# while i > 0:
#     print(f'剩余{i}次机会...')
#     username = input('请输入用户名:')
#     password = input('请输入密码:')
#
#     if username == local_username and password == local_password:
#         print('登录成功...')
#         break
#     else:
#         print('登录失败...')
#     i -= 1
# else:
#     # 循环条件不成立则执行else代码
#     print('今日三次机会已经全部用完, 请明天再试...')

for item in range(3, 0, -1):
    print(f'剩余{item}次机会')
    username = input('请输入用户名:')
    password = input('请输入密码:')

    if username == local_username and password == local_password:
        print('登录成功...')
        break
    else:
        print('登录失败...')
else:
    # 循环条件不成立则执行else代码
    print('今日三次机会已经全部用完, 请明天再试...')

