# -*- coding: utf-8 -*-
# @Time     : 2024/11/27 21:21
# @Author   : Lliaster
# @File     : chongdianx_text.py


import requests

url = 'https://www.360buy.com'

headers = {
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'

}

response = requests.get(url, headers=headers)
print(response.history)


for resp in response.history:
    print(resp.url,resp.status_code,resp.headers)