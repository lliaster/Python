# -*- coding: utf-8 -*-
# @Time    : 2024/9/9 20:17
# @Author  : poppies
# @File    : 2.用户登录案例.py
# @Software: PyCharm


local_name = 'admin'
local_password = '123456'

username = input('请输入用户名: ')
password = input('请输入密码: ')  # 输入的密码的类型是字符串类型

if username == local_name and local_password == password:
    print('登录成功...')

print('if代码执行完毕...')

# 如果大家需要将密码强转为int类型则必须要保证密码中的数据是纯数字
