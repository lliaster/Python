# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 20:26
# @Author  : 顾安
# @File    : 3.类属性.py


"""
实例属性: 一般都是在构造方法中创建
类属性: 一般是一个类的内部变量
"""


class Tool:
    # 定义一个变量
    tools_num = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Tool.tools_num += 1

    def show_tools_1(self):
        # 不要使用self参数尝试对类属性进行修改, 因为self实例会认为要创建一个新的实例属性
        print(f'工具总数为: {self.tools_num}')

    def show_tools_2(self):
        print(f'工具总数为: {Tool.tools_num}')


# 1.类属性可以直接被类对象访问
print(Tool.tools_num)  # 这个没有实例化所以返回的是0

# 2.实例对象访问类属性
tool_1 = Tool('锄头')
tool_2 = Tool('电钻')
tool_3 = Tool('锯子')
print(tool_1.tools_num)

tool_1.show_tools_1()
tool_3.show_tools_2()


"""
1.类属性可以被类对象(类名)和实例对象访问
2.不要尝试使用self修改类属性的值
3.类属性在全局内存中只有一份

类属性的使用场景:
    如果需要保证一个对象/值在全局只有一份的情况下则使用类属性
        比如: 数据库链接对象
"""
