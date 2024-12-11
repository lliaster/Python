# -*- coding: utf-8 -*-
# @Time     : 2024/12/9 21:12
# @Author   : Lliaster
# @File     : test.py

import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "QC005=3c01fe0e14ff6df95a345c335a1fea3b; QC006=ttyhmsdz2r571nshq0ivh9ev; TQC030=1; T00404=9afb91084fac846829f097a88288685e; QP0030=1; QC173=0; P00004=.1704441697.e50aa29dc8; QC160=%7B%22type%22%3A-1%2C%22conformLoginType%22%3A0%7D; QC170=1; QP0035=5; QC219=a021e6d2422def438f8ecd948bbe7dbb4d8074cc1d1a82b9d6dc3da638c7343ab3; QC218=c0f5f47bd0b2b13152efb3c46c7c11e7; QC220=f0a804c01813138f5050b0cff1bd3d31; IMS=IggQABj_58StBioqCiBiNWQ4NDY0Yzg1NDM3NDkyYzg2MDZmZDBmOTE5ODI1ZRAAIgAobjAFciQKIGI1ZDg0NjRjODU0Mzc0OTJjODYwNmZkMGY5MTk4MjVlEACCAQCKASQKIgogYjVkODQ2NGM4NTQzNzQ5MmM4NjA2ZmQwZjkxOTgyNWU; QP0037=5; QP0036=2024124%7C9.875; QIYUECK=qy_pc_e2fa6908be074f048d7fe19e46a5caf7; QP008=1140; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D; QC189=8883_B%2C8185_A%2C8739_B%2C9419_A%2C9379_B%2C9922_B%2C8004_B%2C5257_B%2C9776_B%2C8873_E%2C10123_A%2C7423_C%2C8401_A%2C6249_C%2C7996_B%2C9576_B%2C9365_B%2C5465_B%2C6843_B%2C10096_A%2C6578_B%2C6312_B%2C6091_B%2C8690_A%2C8737_D%2C8742_A%2C9484_B%2C6752_C%2C8971_B%2C7332_B%2C9683_A%2C8665_D%2C6237_B%2C9569_B%2C8983_C%2C7024_C%2C5592_B%2C9117_A%2C6031_B%2C7581_B%2C9506_B%2C9517_A%2C9394_B%2C8542_B%2C6050_B%2C9167_A%2C9469_B%2C8812_B%2C6832_C%2C7074_C%2C7682_C%2C5924_D%2C6151_C%2C5468_B%2C8867_B%2C6704_C%2C8808_B%2C8497_B%2C8342_B%2C8871_C%2C9790_B%2C9355_B%2C8760_B%2C9292_B%2C6629_B%2C5670_B%2C9158_A%2C9805_B%2C9959_B%2C6082_B%2C5335_B; QC198=de7d4a127824614543ffff5b0c7047d3; QC191=; QC007=DIRECT; QC008=1704441629.1706084986.1733749722.3; QC199=544f61aeaccd397753da168cfefdf21f; QC186=false; nu=0; __dfp=a0828a63efb43e4c1aa3a87dbe80ad2e71d516e1bfdd9fbaf488083f53cb476029@1735045722429@1733749723429; QC187=true; QC010=150791607",
    "origin": "https://list.iqiyi.com",
    "priority": "u=1, i",
    "referer": "https://list.iqiyi.com/www/2/15-------------11-1-1-iqiyi--.html?s_source=PCW_SC",
    "sec-ch-ua": "\\Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\\Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
url = "https://pcw-api.iqiyi.com/search/recommend/list"
params = {
    "channel_id": "2",
    "data_type": "1",
    "mode": "11",
    "page_id": "2",
    "ret_num": "48",
    "session": "a07d98ca5c2b92817f02a4d60e31ef78",
    "three_category_id": "15;must"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)