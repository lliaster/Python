# -*- coding: utf-8 -*-
# @Time     : 2024/10/26 15:35
# @Author   : Lliaster
# @File     : test1.py
import requests

file_path = './测试文件.txt'
stu_name_list = ['abc', '\ndef', '\nhh']
# b= open(file_path,mode='r',encoding='utf-8')
# print(b)
# print('内容',b.read())
# b.close()
# c = open(file_path,mode='w+',encoding='utf-8')
# c.write(stu_name_list[0])
# c.close()


with open(file_path, encoding='utf-8', mode='r+') as f:
    f.writelines(stu_name_list)
    f.seek(0)
    print('1', f.read())
with open(file_path, 'r', encoding='utf-8') as e:
    print('2\n', e.read())

image_url = 'https://img.pcauto.com.cn/images/upload/upc/tx/autocms/2307/20/c61/371693421_1689830062607_thumb.jpg'
response = requests.get(image_url).content
print(response)
with open('A07.jpg', 'wb') as i:
    i.write(response)
