# -*- coding: utf-8 -*-
# @Time     : 2024/12/15 00:31
# @Author   : Lliaster
# @File     : test.py

import pymongo
mongo_client = pymongo.MongoClient()
collection = mongo_client['py_spider']['process_tx_work']




file_path = r"D:\爬虫图片\['源纱希喵喵喵 作品合集 [百度云合集] - 老婆不在家']\16001415844.jpg"

# 替换路径中的特殊字符
file_path = file_path.replace("'", "").replace("[", "").replace("]", "")

if os.path.exists(file_path):
    print("文件存在")
else:
    print("文件不存在")