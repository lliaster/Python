# -*- coding: utf-8 -*-
# @Time     : 2024/11/25 20:52
# @Author   : Lliaster
# @File     : requests_test_image.py

import requests
url = 'https://img1.baidu.com/it/u=1494974577,3964476210&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=889'
img = requests.get(url).content
print(img)
with open('jk.png', 'wb') as f:
    f.write(img)