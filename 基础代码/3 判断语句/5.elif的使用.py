# -*- coding: utf-8 -*-
# @Time    : 2024/9/9 20:36
# @Author  : poppies
# @File    : 5.elif的使用.py
# @Software: PyCharm


"""
elif可以完成if判断的条件分支
"""

"""
if 条件1:
    条件1成立要执行的代码
elif 条件2:
    条件2成立要执行的代码
elif 条件3:
    条件3成立要执行的代码
    ...
else:
    以上条件都不成立则执行else之下的代码
"""

# 判断一位学生考试的分数位于哪个等级

score = -1

if score >= 90 and score <= 100:  # 如果分数在90~100
    print('本次考试，等级为A')
elif score >= 80 and score < 90:  # 如果分数在80~90
    print('本次考试，等级为B')
elif score >= 70 and score < 80:  # 如果分数在70~80
    print('本次考试，等级为C')
elif score >= 60 and score < 70:  # 如果分数在60~70
    print('本次考试，等级为D')
elif score >= 0 and score < 60:  # 如果分数在60以下
    print('本次考试，等级为E')
else:  # 如果分数不在0~100之间，就认为错误
    print("分数有误...")


"""
总结:
    1.if语句结构: if...elif...else
    2.elif 后面也需要跟上一个条件
    3.elif与else关键字不能单独使用, 需要配合if语句
"""
