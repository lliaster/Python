# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 20:59
# @Author  : poppies
# @File    : 8.将函数引用保存在列表中.py
# @Software: PyCharm


def get_info(url):
    print(url)


url_1 = 'https://www.baidu.com/'
url_2 = 'https://www.goole.com/'
url_3 = 'https://www.bing.com/'

method_list = [get_info for _ in range(3)]

for m in method_list:
    m(url_1)
    m(url_2)
    m(url_3)
