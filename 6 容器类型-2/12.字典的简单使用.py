# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 21:50
# @Author  : poppies
# @File    : 12.字典的简单使用.py
# @Software: PyCharm


stu_info = {
    'name': '安娜',
    'age': 18,
    'gender': '女',
    'address': '长沙'
}


# 字典遍历
for item in stu_info:
    print(item)  # 返回的值是字典的key, 并没有value


# 字典是可以和其他数据结构完成嵌套的
cls_info = {
    'stu_names': ['张三', '李四', '王五'],
    'stu_age': (18, 19, 20)
}

# 在字典中获取指定的value需要根据key获取
# cls_info['key_name']
print(cls_info['stu_names'])
print(cls_info['stu_age'])


# 字典中的key必须保证唯一, 必须是不可变对象
# stu_info = {
#     'username': '安娜',
#     'username': '双双'
# }

stu_info = {
    ('username',): '安娜',
    'username': '双双'
}
print(stu_info)


stu_info = [
    {'user_name': '安娜'},
    {'user_name': '双双'}
]

for item in stu_info:
    print(item['user_name'])


"""
总结：
    1.字典的key必须是唯一的并且不可变
    2.字典的数据结构相对灵活, 可以搭配不同的数据结构完成数据嵌套
    3.直接对字典进行遍历获取到的结果只是字典中的key, 无法获取value
"""

