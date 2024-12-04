# -*- coding: utf-8 -*-
# @Time     : 2024/11/30 21:48
# @Author   : Lliaster
# @File     : text2qingting.py

import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "msite_id=725148b7-1478-4082-91a0-242a97a547ae; HWWAFSESID=4b98073b3e20817b47; HWWAFSESTIME=1732974397984; INGRESSCOOKIE=1732974398.996.131769.791092|9c92c5a980a2afb7a7f825c58c40b9de; _ga_F11JB62JM2=GS1.1.1732974374.1.0.1732974374.0.0.0; _ga=GA1.2.1748032517.1732974375; _gid=GA1.2.379907234.1732974375; _gat_gtag_UA_148368616_2=1",
    "Origin": "https://m.qingting.fm",
    "Referer": "https://m.qingting.fm/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}
url = "https://webapi.qingting.fm/api/mobile/rank/hotSaleWeekly"
response = requests.get(url, headers=headers)
# print(response.json())
# print(response.text)
# print(response)


for item in response.json()['rankinglist']:
    # print(item['title'])
    temp_dict = dict()
    temp_dict['title']=item['title']
    temp_dict['desc']=item['desc']
    temp_dict['imgUrl']=item['imgUrl']

