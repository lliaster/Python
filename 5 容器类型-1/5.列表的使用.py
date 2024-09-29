# -*- coding: utf-8 -*-
# @Time    : 2024/9/13 21:20
# @Author  : poppies
# @File    : 5.列表的使用.py
# @Software: PyCharm

# 保存三名学生
stu_names = ['张三', '李四', '王五', '赵六']

# 列表支持迭代
for name in stu_names:
    print(name)
print('-' * 30)
print(stu_names[1])  # 列表支持切片

# 列表的元素修改
stu_names[0] = '安娜'
print(stu_names)

# 切片的使用
# 如果对列表进行切片那么会返回一个新列表
# 切片之后不会对原有列表造成影响
new_list = stu_names[1:3]
print(new_list, stu_names)

print('-' * 30)

# 列表倒序
new_list = stu_names[::-1]
print(new_list, stu_names)


# 使用while循环对列表迭代
"""
print
type
input
range
len: 可以获取到一个容器类型的长度
"""
list_length = len(stu_names)
i = 0
while i < list_length:
    print(stu_names[i])
    i += 1



