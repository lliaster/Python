# -*- coding: utf-8 -*-
# @Time    : 2024/11/9 20:45
# @Author  : 顾安
# @File    : 4.数据插入.py


import pymysql
import datetime


def insert_info():
    with pymysql.connect(host='localhost', user='root', password='root', db='python_test_1') as db:
        with db.cursor() as cursor:
            sql = """
                insert into employee values (
                    %s, %s, %s, %s, %s, %s
                );
            """

            try:
                info = ('安', '娜', 19, '女', 17000, datetime.datetime.now())
                cursor.execute(sql, info)

                # 涉及到数据插入需要进行事务的提交: 链接对象才有事务提交的功能
                db.commit()
                print('数据插入成功:', info)
            except Exception as e:
                print('数据插入失败:', e)

                # 如果失败需要回滚
                db.rollback()


insert_info()
