# -*- coding: utf-8 -*-
# @Time    : 2024/11/9 20:24
# @Author  : 顾安
# @File    : 2.数据库的连接.py


# pip install pymysql
import pymysql


def db_connect():
    # 1.创建链接对象
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python_test_1')

    # 2.创建游标(游标对象用于执行sql代码)
    cursor = db.cursor()

    # 3.执行sql
    sql = 'select * from students;'
    cursor.execute(sql)

    # 4.获取执行结果
    # result = cursor.fetchone()
    # for row in result:
    #     print(row)

    # result_tuple = cursor.fetchall()
    # for row in result_tuple:
    #     print(row)

    result_tuple = cursor.fetchmany(5)
    print(result_tuple)

    # 5.关闭链接对象和游标对象
    cursor.close()
    db.close()


db_connect()
