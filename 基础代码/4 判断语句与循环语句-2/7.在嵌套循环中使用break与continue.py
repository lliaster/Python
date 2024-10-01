# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 21:19
# @Author  : poppies
# @File    : 7.在嵌套循环中使用break与continue.py
# @Software: PyCharm


"""
break终止当前所在的循环
    如果当前的循环在另外一个循环的内部则不会影响外层循环
"""

# i = 0
# while i < 10:
#     print(f'i的值为: {i}')
#     i += 1
#
#     while True:
#         print('这是内部循环打印的信息...')
#         break


# i = 0
# while i < 10:
#     print(f'i的值为: {i}')
#     i += 1
#
#     j = 0
#     while j < 10:
#         print('这是内部循环打印的信息...')
#         j += 1
#         continue
#         print('这是在continue之下所需要打印的信息...')
#     print('这是外层循环需要打印的信息...')  # 外层循环的代码不会收到内部循环中的continue的影响


for i in range(10):
    print(f'i={i}')
    for j in range(3):
        print(f'j={j}')
        break  # break不会对外层for循环产生影响
