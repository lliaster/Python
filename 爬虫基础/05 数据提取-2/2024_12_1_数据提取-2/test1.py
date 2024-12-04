# -*- coding: utf-8 -*-
# @Time     : 2024/12/2 21:06
# @Author   : Lliaster
# @File     : test1.py

import  requests
from lxml import etree

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers).text
tree = etree.HTML(response)
print(response)