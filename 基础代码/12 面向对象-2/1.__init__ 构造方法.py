# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 20:05
# @Author  : poppies
# @File    : 1.__init__ 构造方法.py
# @Software: PyCharm


"""
1.__init__是一种特殊的魔术方法
    魔术方法是python这门语言自带的一些方法, 不是开发者创建的, 自带的, 不能擅自修改魔术方法名

2.魔术方法无需开发者手动调用

3.__init__方法在类的实例化过程中只会被执行一次
"""


# pip install fake_useragent
from fake_useragent import UserAgent


class MyUserAgent:
    # 构造方法在实例化时只会被执行一次
    def __init__(self):
        self.headers = UserAgent().random  # 执行一次


my_user_agent = MyUserAgent()

print(my_user_agent.headers)
print(my_user_agent.headers)
print(my_user_agent.headers)



