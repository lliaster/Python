# -*- coding: utf-8 -*-
# @Time    : 2024/10/23 20:16
# @Author  : 顾安
# @File    : 4.写入图片数据


import requests

image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.alicdn.com%2Fbao%2Fuploaded%2Fi3%2F67303687%2FO1CN01UhU0rw1d6h0XuRL9S_%21%2167303687.jpg&refer=http%3A%2F%2Fimg.alicdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1732277722&t=eb48a8b639557e09a91a93d3d97fb170'
response = requests.get(image_url).content
# print(response)

# wb: 二进制覆盖写
# ab: 二进制追加写
with open('汉服.jpg', 'wb') as f:
    f.write(response)
