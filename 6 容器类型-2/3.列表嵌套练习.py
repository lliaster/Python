# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 20:12
# @Author  : poppies
# @File    : 3.列表嵌套练习.py
# @Software: PyCharm


# 标准库: 产生随机数
import random


offices = [[], [], []]
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 将老师列表进行遍历获取每一个老师完成办公室的分配
for name in names:
    # 使用random生成三个办公室的索引
    random_index = random.randint(0, 2)
    offices[random_index].append(name)


# 定义办公室编号
office_index = 1
for office in offices:
    print(f'办公室编号为: {office_index}, 人数为: {len(office)}')
    office_index += 1

    for name in office:
        print(f'{name}', end=' ')
    print()
    print('-' * 30)

