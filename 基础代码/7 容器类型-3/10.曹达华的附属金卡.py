# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 21:53
# @Author  : poppies
# @File    : 10.曹达华的附属金卡.py
# @Software: PyCharm


card = ["女警司", 20200520, [200000, 15000]]
c_card = card.copy()

c_card[0] = '曹达华'
c_card[1] = 20200521


# 曹达华使用了1000块
c_card[2][1] -= 1000
print('曹达华:', c_card)
print('女警司:', card)
