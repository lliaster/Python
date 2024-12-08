# -*- coding: utf-8 -*-
# @Time     : 2024/12/8 17:21
# @Author   : Lliaster
# @File     : bilibili_test.py


import csv
import requests

url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?category_id=&search_type=video&ad_resource=5654&__refresh__=true&_extra=&context=&page={}&page_size=42&pubtime_begin_s=0&pubtime_end_s=0&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E4%B8%9C%E6%96%B9%E5%AF%92%E5%85%94&qv_id=5crmTgYPF2jM0G0OFvqRU9ZWQGlmsSvf&source_tag=3&gaia_vtoken=&dynamic_offset=150&web_location=1430654&w_rid=0791be58b9ae96b8cc12cbd402cfdd69&wts=1733649156'
headers = {'cookie':
"i-wanna-go-back=-1; DedeUserID=13557210; DedeUserID__ckMd5=5bd1d1e2e20d4f18; CURRENT_BLACKGAP=0; buvid4=88849BD8-9571-FB3B-C17E-C1254E68E9C281922-023021816-qW%2FmFcO1WNF3ADltVvggLQ%3D%3D; buvid_fp_plain=undefined; enable_web_push=DISABLE; is-2022-channel=1; _uuid=8856AED1-6C77-512B-AB21-97BFA674AE7D56978infoc; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW; hit-dyn-v2=1; buvid3=A28EF32E-6880-3863-B6FE-2BFE6F25422A32387infoc; b_nut=1711283932; b_ut=5; header_theme_version=CLOSE; rpdid=|(k|lmll|R))0J'u~uuk)Ru)u; LIVE_BUVID=AUTO6417178186166535; PVID=1; fingerprint=a5ecbe5a664ac737d7c679c05a7153f1; buvid_fp=a5ecbe5a664ac737d7c679c05a7153f1; CURRENT_QUALITY=80; SESSDATA=d6180225%2C1748951763%2C623a8%2Ac1CjDvtxc5cLNocoIDENvLV6BxnL0D6u4CwZx80mYh6vQeNa8FGnKwR_gNlC08Y0M6TYcSVnloWWFDVkRPTWZ1QlpkanZqX2EyN19XcUs1WktDemkxSVA3X1ozUENiSW5jLUVSU3NUUm9BUk81bUZKLTdnWEpTMTA4M2dNLVI2bG9Kb0N0ZVM3UFB3IIEC; bili_jct=1df8708393bfedd746930a00c4e77d62; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzM3NTQyMTYsImlhdCI6MTczMzQ5NDk1NiwicGx0IjotMX0.HLCmaPdF9aSP35NIxx50U9mxeS74pWCw9bKVMU-IL4c; bili_ticket_expires=1733754156; bp_t_offset_13557210=1008452909442007040; b_lsid=8E5BEE8C_193A5672B08; home_feed_column=4; browser_resolution=1374-1047; sid=8m2ylnj9; CURRENT_FNVAL=4048",
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}


response = requests.get(url, headers=headers)
# print(response.json())


def save_csv_bilibli_video_info(api_url):
        field_name = ['title', 'author']
        with open('bilibili_video_info.csv', 'w', newline='', encoding='utf-8') as f:
            f_csv = csv.DictWriter(f, field_name)
            f_csv.writeheader()

            for page in range(1, 2):
                response = requests.get(api_url.format(page), headers=headers).json()
                for temp in response['data']['result']:

                    item = dict()
                    item['title'] = temp['title']
                    item['author'] = temp['author']
                    print(item)
                    f_csv.writerow(item)

save_csv_bilibli_video_info(url)