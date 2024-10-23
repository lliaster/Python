# -*- coding: utf-8 -*-
# @Time    : 2024/10/21 20:44
# @Author  : 顾安
# @File    : 5.断言


import requests
from requests.exceptions import HTTPError

url = 'https://www.baidu.com/abc'
response = requests.get(url)

# 断言
# 断言可以让原本不报错的代码强制报错
"""
assert 判断条件, 异常对象
"""
assert response.status_code == 200, HTTPError
