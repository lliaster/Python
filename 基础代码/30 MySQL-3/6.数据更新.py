# -*- coding: utf-8 -*-
# @Time    : 2024/11/9 20:58
# @Author  : 顾安
# @File    : 6.数据更新.py


import pymysql


def update_info():
    with pymysql.connect(host='localhost', user='root', password='root', db='python_test_1') as db:
        with db.cursor() as cursor:
            sql = 'update employee set income = income + 3000 where sex = "女";'
            try:
                cursor.execute(sql)
                db.commit()
                print('数据更新成功...')
            except Exception as e:
                print('数据更新失败:', e)
                db.rollback()


update_info()
