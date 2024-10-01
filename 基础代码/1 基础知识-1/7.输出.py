# -*- coding: utf-8 -*-
# @Time    : 2024/9/4 21:31
# @Author  : poppies
# @File    : 7.输出.py
# @Software: PyCharm


"""
print内置函数可以打印信息
"""

num = 10
print(num)

# 打印表达式计算出的结果
print(100 + 200)

# 如果字符串使用 + 则表示字符串拼接
print('100' + '200' + '300')  # 如果一个数据的左右两边有单引号/双引号则这个数据就是字符串
# 当前字符串中的空格也是字符串
print('100 + 200 + 300')

num1 = 1
num2 = 2
num3 = 3
# print打印多个值可以通过逗号进行分割
print(num1, num2, num3)


"""
字符串格式化
"""
# % 表达式
str_data = '小明今年10岁啦'
print(str_data)

name = '小红'
age = 12
str_data = '%s今年%d岁啦' % (name, age)
print(str_data)


# f表达式
name = '小蓝'
age = 13
str_data = f'{name}今年{age}岁啦'
print(str_data)


# format格式化
name = '安娜老师'
age = 18
email_address = 'anna.teacher@gmail.com'

str_data = '我是{}老师, 今年{}岁, 邮箱是:{}'.format(name, age, email_address)
print(str_data)

# 浮点类型格式化
num = 3.1415926

# 保留小数点两位输出
str_data = '圆周率: %.2f' % num  # 支持四舍五入
print(str_data)

str_data = f'圆周率: {num:.2f}'
print(str_data)

str_data = '圆周率: {:.2f}'.format(num)
print(str_data)








