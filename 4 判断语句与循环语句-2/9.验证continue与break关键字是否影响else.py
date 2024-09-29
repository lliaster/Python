# -*- coding: utf-8 -*-
# @Time    : 2024/9/11 21:38
# @Author  : poppies
# @File    : 9.验证continue与break关键字是否影响else.py
# @Software: PyCharm

# i = 0
# while i < 3:
#     i += 1
#     print('打印的信息 - 1')
#     continue  # continue不会影响else中的代码
#     print('打印的信息 - 2')
# else:
#     print('打印的信息 - 3')


i = 0
while i < 3:
    i += 1
    print('打印的信息 - 1')
    break  # 因为break会直接终止循环的运行, 所以会影响到else代码的执行
    print('打印的信息 - 2')
else:
    print('打印的信息 - 3')
