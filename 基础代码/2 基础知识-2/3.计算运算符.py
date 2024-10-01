# -*- coding: utf-8 -*-
# @Time    : 2024/9/6 20:56
# @Author  : poppies
# @File    : 3.计算运算符.py
# @Software: PyCharm


num1 = 9
num2 = 2

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

print(num1 / num2)
print(num1 % num2)  # 取余数
print(num1 // num2)  # 取整数

# 计算的优先级: ()
print(10 + 5 * 2)
print((10 + 5) * 2)

# 批量赋值
n1, n2, n3 = 1, 2, 3
print(n1, n2, n3)

# 复合赋值运算符
num = 10
print(num)

# num = 10 + 1
# print(num)

num += 1
print(num)

num -= 1
# num = num - 1
print(num)


