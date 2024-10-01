# -*- coding: utf-8 -*-
# @Time    : 2024/9/9 21:07
# @Author  : poppies
# @File    : 7.while循环练习.py
# @Software: PyCharm


# 打印五次你想要输出的信息
# i = 1
# while i <= 5:
#     print('双双胖三斤...')
#     i += 1  # 执行一次计数器 + 1, 加到一定次数可以让循环终止


# 1 + 2 + 3 + 4 ... + 100
# sum_result = 0
#
# i = 1
# while i <= 100:
#     sum_result += i
#     i += 1
#
# print(sum_result)

# 1 - 100 中所有的偶数的和
# sum_result = 0
# i = 1
# while i <= 100:
#     # 计数器的值除以2得到的余数为0则就是偶数
#     if i % 2 == 0:
#         sum_result += i
#
#     # if条件是否成立都需要执行计数器 + 1
#     i += 1
#
# print(sum_result)


# 计算1 - 100序列中的元素除以3余数为0和除以7余数为0的累加和
num_result = 0
i = 1
while i <= 100:
    if i % 3 == 0 and i % 7 == 0:
        num_result += i

    i += 1

print(num_result)







