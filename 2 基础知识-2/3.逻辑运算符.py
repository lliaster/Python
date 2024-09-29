# -*- coding: utf-8 -*-
# @Time    : 2024/9/6 21:28
# @Author  : poppies
# @File    : 3.逻辑运算符.py
# @Software: PyCharm


"""
在多个判断条件的场景下会使用逻辑运算符
"""

# and是用于链接多个条件并且要保证所有条件都为真才返回True
print(100 > 50 and 90 < 200)
print(100 < 50 and 90 < 200)

# or: 多个条件只要成立一个则整体条件返回真, 所有条件都不成立则整体返回False
print(100 < 50 or 90 < 200)
print(100 < 50 or 90 > 200)

# not: 取反, 如果表达式返回的值为True则not获取到的结果为False, 如果表达式返回的结果为False则not获取的结果为True
print(not 100 > 90)
print(not 100 < 90)

"""
总结：
    and、or、not
    
    and: 所有条件全部成立则返回True
    or: 其中一个条件成立则返回True
    not: 根据表达式返回的结果取反
"""


