# -*- coding: utf-8 -*-
# @Time    : 2024/11/9 20:54
# @Author  : 顾安
# @File    : 5.数据查询.py


import pymysql


def search_info():
    with pymysql.connect(host='localhost', user='root', password='root', db='python_test_1') as db:
        with db.cursor() as cursor:
            sql = 'select * from employee where income > %s' % 10000

            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except Exception as e:
                print('查询失败:', e)


search_info()