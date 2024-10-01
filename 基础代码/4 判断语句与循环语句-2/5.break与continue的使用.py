# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 20:43
# @Author  : poppies
# @File    : 5.break与continue的使用.py
# @Software: PyCharm


"""
while
for
if
else
elif

in: 成员运算符
break: 终止循环
continue: 忽略本次循环
"""

# int_list = [1, 2, 3, 4, 5]
# num = 3

# in关键字可以判断一个值是否在另一个容器中存在
# print(num in int_list)


# 如果判断出num在int_list内部则直接中断循环
# num = 2
# int_list = [1, 2, 3, 4, 5]

# break
# for item in int_list:
#     if item == num:
#         print('已经找到了...')
#         break  # 如果条件成立则直接中断循环
#     else:
#         print(item)


# for item in int_list:
#     if item == num:
#         print('已经找到了...')
#         continue  # 忽略本次循环(如果continue之下有代码则不会执行代码), 不会导致循环终止
#         print('这是一个测试信息...')  # 当前代码永远不会被执行
#     else:
#         print(item)


# i = 0
# while i < 10:
#     print(i)
#     i += 1
#     if i == 6:
#         break

i = 0
while i < 10:
    i += 1
    if i == 6:
        continue
    else:
        print(f'这是循环中的字符串: {i}')
