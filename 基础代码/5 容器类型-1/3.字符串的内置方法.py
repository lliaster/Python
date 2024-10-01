# -*- coding: utf-8 -*-
# @Time    : 2024/9/13 20:33
# @Author  : poppies
# @File    : 3.字符串的内置方法.py
# @Software: PyCharm


# find
my_str = 'welcome to www.tulingxueyuan.com'
print(my_str.find('to'))  # 返回的结果是当前英文单词的首字母索引

# rfind: 从右往左查询
print(my_str.rfind('to'))

# count: 统计出现的元素次数
print(my_str.count('w'))

# replace: 字符串替换
print(my_str.replace('w', 'W'))
print(my_str.replace('w', 'W', 1))

# split: 字符串分割
my_str = 'welcome to www.tulingxueyuan.com'
print(my_str.split(' '))  # 分割出来的结果是一个列表中的元素
print(my_str.split(' ')[0])

# startswith: 判断你输入字符串是否是另外一个字符串的开头
print(my_str.startswith('m'))
print(my_str.startswith('a'))
print(my_str.startswith('welcome'))

# endswith: 判断你输入字符串是否是另外一个字符串的结尾
print(my_str.endswith('m'))
print(my_str.endswith('w'))

# lower: 将字符串中的元素全部转为小写
my_str = "WELCOME to www.tulingxueyuan.com"
print(my_str.lower())

# upper: 将字符串中的元素全部转为大写
print(my_str.upper())

# strip: 删除字符串两端的空白字符
my_str = "   welcome to www.tulingxueyuan.com   "
print(my_str)
print(my_str.strip())

# partition: 字符串分割: 了解即可
print(my_str.strip().partition('to'))

# splitlines: 根据行分割
my_str = """welcome to www.tulingxueyuan.com
thank you
good good study day day up
"""
print(my_str.splitlines())

# isalpha: 判断字符串中的元素是否全部都是字母
my_str = "abc123"
print(my_str.isalpha())
my_str = "abc"
print(my_str.isalpha())

# isdigit: 判断字符串中的元素是否全部都是数字
my_str = "abc123"
print(my_str.isdigit())
my_str = "123"
print(my_str.isdigit())

# isalnum: 判断字符串中的元素是否全部都是字母或者数字
my_str = "abc123_"
print(my_str.isalnum())

# join: 字符串拼接
str_list = ['welcome', 'to', 'www.tulingxueyuan.com']
str_join = '-'
print(str_join.join(str_list))

