# -*- coding: utf-8 -*-
# @Time    : 2024/11/9 21:01
# @Author  : 顾安
# @File    : 7.数据删除.py


import pymysql


def delete_info():
    with pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python_test_1') as db:
        with db.cursor() as cursor:
            sql = 'delete from employee where age > 18;'

            try:
                cursor.execute(sql)
                db.commit()
                print('数据删除成功...')
            except Exception as e:
                print('代码异常:', e)
                db.rollback()


delete_info()
