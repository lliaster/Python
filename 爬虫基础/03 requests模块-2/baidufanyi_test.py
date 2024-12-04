# -*- coding: utf-8 -*-
# @Time     : 2024/11/27 20:55
# @Author   : Lliaster
# @File     : baidufanyi_test.py


import requests

url = 'https://fanyi.baidu.com/basetrans'

from_data = {
    'query': 'happy',
    'from': 'en',
    'to': 'zh',
    'token': '3c323be6bcc8fb4028ad752cc5932cc6',
    'sign': 221212.492333
}

headers = {
    'user-agent':
        'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'cookie': 'BIDUPSID=BF671075AEFE4F7B7946E44B0E061331; PSTM=1710580942; BAIDUID=BF671075AEFE4F7BB4878E9F4C864B7D:FG=1; BAIDUID_BFESS=BF671075AEFE4F7BB4878E9F4C864B7D:FG=1; ZFY=WofnyBUenwmfH:ALLcXeo8Y0GAPrLoCVilp527G:BAdXc:C; H_PS_PSSID=61027_61089_60851_61130_61113_61140_61160_61176_61206_61212_61214_61230_61245; RT="z=1&dm=baidu.com&si=edf7916a-f033-45f0-ad3b-0173fc7e3105&ss=m3zvy0s0&sl=1&tt=1jn&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&r=sl7uja1&ul=8hw&hd=8l6"; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1732711943; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1732711943; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1732711943; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1732711943; ab_sr=1.0.1_NWYxMWVhNGU2ODM5MzlmNjMxYzliYTA3NTk1ZWM0NTYzYTAyMmRhN2Q5YjFlZjMxZGY2MDRkYWI5YTRiNWMxZjk2MTAwMjg2Yjc4YzM1M2Y1MDI4MzJmNmRjZDk3ZTVmMWMzYTFmY2QxMzMxZDU0OGQ0OGRiNzc0MTU1ZjgyZDJiNTI5YmE0OGZlZGRlZWQ5M2ZlOGZkZTdlNDY1YmI4ZmNkOTZhZjE2ZjgzY2UxY2FiODI5YWM5ZDkzOWU5ZjNmOGEzYTBjODJlMTM5YTMzMDIxNzBiODYyYjg3YTEyMTU='
}


response = requests.post(url, headers=headers, data=from_data).json()

print(response)
