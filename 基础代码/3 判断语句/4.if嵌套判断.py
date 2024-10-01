# -*- coding: utf-8 -*-
# @Time    : 2024/9/9 20:28
# @Author  : poppies
# @File    : 4.if嵌套判断.py
# @Software: PyCharm


"""
安娜要坐高铁回家
    1.安检
    2.检票
"""

"""
if 条件1:
    if 条件2:
        条件2成立时执行的代码...
    else:
        条件2不成立时执行的代码...
else:
    条件1不成立时要执行的代码...
"""

chepiao = False
daoju = 9


if daoju <= 9:
    print('安检通过...')
    # if chepiao == True:
    if chepiao:
        print('已有车票, 可以上车...')
    else:
        print('暂无车票, 禁止上车...')
else:
    print('危险, 禁止进站...')


