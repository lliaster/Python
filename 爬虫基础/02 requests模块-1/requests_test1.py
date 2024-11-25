# -*- coding: utf-8 -*-
# @Time     : 2024/11/25 19:47
# @Author   : Lliaster
# @File     : requests_test1.py



import requests

url = 'https://www.baidu.com'

# response = requests.get(url).text
response = requests.get(url).content
print(response.decode('utf-8'))



print('x'*33)

str_data = 'abc'
bytes_data = str_data.encode('gbk')#编码
print(bytes_data)
print(bytes_data.decode('gbk'))#解码

print('x'*33)
url = 'https://www.baidu.com'
response =  requests.get(url)
print(response.status_code)
print(response.content) # 乱码,写图片,视频,音频用
print(response.text)
print(response.content.decode())

print('x'*88)

print(response.request.headers)
print(response.headers['Set-Cookie'])
print(response.cookies)
print(dict(response.cookies))
print(response.url)
print(response.request.url)

print(response.content.decode())
response.encoding = 'utf-8'
print(response.text)
