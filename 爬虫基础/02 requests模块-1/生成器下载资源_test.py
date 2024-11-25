# -*- coding: utf-8 -*-
# @Time     : 2024/11/25 21:00
# @Author   : Lliaster
# @File     : 生成器下载资源_test.py
import requests
image_url = 'https://img1.baidu.com/it/u=1494974577,3964476210&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=889'

response = requests.get(image_url,stream=True)

with open('jk_2.png','wb') as file:
    for chunk in response.iter_content(chunk_size=102400):
        file.write(chunk)