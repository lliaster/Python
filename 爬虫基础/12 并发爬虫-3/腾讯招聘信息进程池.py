# -*- coding: utf-8 -*-
# @Time     : 2024/12/15 00:11
# @Author   : Lliaster
# @File     : 腾讯招聘信息进程池.py
from pydoc import pager

# -*- coding: utf-8 -*-
# @Time    : 2024/12/12 20:40
# @Author  : 顾安
# @File    : 4.使用进程的方式获取腾讯招聘信息.py


import pymongo
import requests
import jsonpath
from multiprocessing import Process, JoinableQueue as Queue
from concurrent.futures import ProcessPoolExecutor, wait
from multiprocessing import Manager

url = "https://careers.tencent.com/tencentcareer/api/post/Query"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

mongo_client = pymongo.MongoClient('mongodb://192.168.1.14:27017')
collection = mongo_client['py_spider']['process_tx_work']


def get_work_info(page_num, q):
    params = {
        "timestamp": "1734007336709",
        "countryId": "",
        "cityId": "",
        "bgIds": "",
        "productId": "",
        "categoryId": "",
        "parentCategoryId": "",
        "attrId": "",
        "keyword": "python",
        "pageIndex": page_num,
        "pageSize": "10",
        "language": "zh-cn",
        "area": "cn"
    }

    response = requests.get(url, headers=headers, params=params).json()
    try:
        for info in response['Data']['Posts']:
            work_info_dict = dict()
            work_info_dict['recruit_post_name'] = jsonpath.jsonpath(info, '$..RecruitPostName')[0]
            work_info_dict['country_name'] = jsonpath.jsonpath(info, '$..CountryName')[0]
            work_info_dict['location_name'] = jsonpath.jsonpath(info, '$..LocationName')[0]
            work_info_dict['category_name'] = jsonpath.jsonpath(info, '$..CategoryName')[0]
            work_info_dict['responsibility'] = jsonpath.jsonpath(info, '$..Responsibility')[0]
            work_info_dict['last_update_time'] = jsonpath.jsonpath(info, '$..LastUpdateTime')[0]
            q.put(work_info_dict)
            print('当前页数:',page_num,'当前页面数据:',work_info_dict)
    except TypeError:
        print('数据不存在:', params.get('pageIndex'))


def save_work_info(q):
    while True:
        dict_info = q.get()
        if dict_info is not None:
            collection.insert_one(dict_info)
            print('数据插入成功:', dict_info)
        else:
            break


def main():
    print('主程序启动...')
    with Manager() as manager:
        queue = manager.Queue()
        with ProcessPoolExecutor() as pool:
            for page in range(1, 36):
                future = pool.submit(get_work_info,page,queue)
            pool.submit(save_work_info, queue)

            wait([future])  # 必须要等待进程1的任务全部完成之后才能让主进程传送None给队列
            queue.put(None)


if __name__ == '__main__':
    main()



'''
if __name__ == '__main__':
    dict_info_queue = Queue()

    process_list = list()
    for page in range(1, 35):
        p_get_info = Process(target=get_work_info, args=(page, dict_info_queue))
        process_list.append(p_get_info)

    p_save_work = Process(target=save_work_info, args=(dict_info_queue,))

    for process_obj in process_list:
        process_obj.start()

    p_save_work.daemon = True  # 设置守护进程
    p_save_work.start()

    for process_obj in process_list:
        process_obj.join()

    # 当队列计数器为0则释放主线程
    dict_info_queue.join()

    print('任务完成...')
'''
"""
家庭作业:
    1.将上述代码修改成进程池
        在进程池中需要使用Manager创建队列对象

    2.使用线程的方式获取网站图片并保存
        请求地址: https://www.lpbzj.vip/allimg
        要求: 进入到详情页并获取所有图片资源并保存到本地

        作业完成后截图你保存的图片文件夹私发企业微信即可！！！
"""
