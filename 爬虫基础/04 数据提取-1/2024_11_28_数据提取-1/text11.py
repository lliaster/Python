# -*- coding: utf-8 -*-
# @Time     : 2024/11/30 21:39
# @Author   : Lliaster
# @File     : text11.py



import requests
import json


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "JSESSIONID=047FC174B241B4CED4E486C92F245EC9; SF_cookie_4=17470996; _sp_ses.2141=*; _sp_id.2141=b7941e01-6265-4e80-a75a-9ff2ab524b7c.1732544635.2.1732973931.1732544729.3b6b94cf-0f0b-436a-8857-8df91dfa44e7; insert_cookie=45380249; routeId=.uc1",
    "Origin": "http://www.cninfo.com.cn",
    "Referer": "http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}
url = "http://www.cninfo.com.cn/new/disclosure"
data = {
    "column": "szse_latest",
    "pageNum": "1",
    "pageSize": "30",
    "sortName": "",
    "sortType": "",
    "clusterFlag": "true"
}
response = requests.post(url, headers=headers, data=data).json()

print(response)
print(type(response))