# -*- coding: utf-8 -*-
# @Time    : 2024/9/13 21:33
# @Author  : poppies
# @File    : 6.列表的内置方法.py
# @Software: PyCharm


stu_names = ['张三', '李四', '王五', '赵六']

"""
添加元素
"""
# append: 增加一个元素, 添加的元素一定在这个列表的末尾
stu_names.append('安娜')
print(stu_names)

# extend: 可以批量添加多个元素, 传递的参数必须是一个迭代对象
# 可以被for循环执行的对象就是迭代对象
# new_stu_list = ['双双', '夏洛', '南枫']
# 当前添加的元素顺序和append一致, 一定在原有列表元素的末尾
str_data = 'abc'
stu_names.extend(str_data)
print(stu_names)

# insert: 指定索引位置完成元素的插入
new_stu = '何老师'
stu_names.insert(0, new_stu)
print(stu_names)

"""
修改元素
"""
# 在修改元素之前要找你要修改的元素的位置
stu_names[1] = '百川'
print(stu_names)


"""
查询元素
"""
# in: 成员运算符
stu_name = '小冉'
print(stu_name in stu_names)
stu_name = '何老师'
print(stu_name in stu_names)

if stu_name in stu_names:
    print('找到了...')
else:
    print('没找到...')

# count: 统计列表元素的个数
print(stu_names.count('安娜'))
stu_names.append('安娜')
print(stu_names)
print(stu_names.count('安娜'))

# index: 返回你指定的元素的下标
print(stu_names.index('安娜'))  # 返回了第一次出现的元素的下标
# print(stu_names.index('admin'))  # 如果元素不存在会报错


"""
数据删除
"""
movie_names = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print(movie_names)
# del是python中的关键字, 可以删除任意对象, 包活列表和列表元素
del movie_names[3]  # 会影响到原有列表的值
print(movie_names)

# pop: 默认情况下将列表中最后一个元素弹出并可以赋值给一个新的变量
movie_name = movie_names.pop()
print('列表:', movie_names)
print('变量:', movie_name)
movie_name = movie_names.pop(2)  # 指定想要弹出的元素的下标
print('列表:', movie_names)
print('变量:', movie_name)

# remove: 指定元素名称删除
print(movie_names)
movie_names.remove('骇客帝国')
print(movie_names)






