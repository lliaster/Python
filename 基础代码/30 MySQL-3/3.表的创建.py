# -*- coding: utf-8 -*-
# @Time    : 2024/11/9 20:37
# @Author  : 顾安
# @File    : 3.表的创建.py


import pymysql


def create_table():
    with pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python_test_1') as db:
        with db.cursor() as cursor:
            # 创建员工表
            cursor.execute("drop table if exists employee;")

            sql = """
                create table employee(
                    first_name varchar(20) not null,
                    last_name varchar(20),
                    age int,
                    sex varchar(1),
                    income float,
                    create_time datetime
                );
            """

            # 执行sql可能会出现异常, 所以建议使用try捕获异常
            try:
                cursor.execute(sql)
                print('表创建成功...')
                # db.commit()  表的创建无需提交事务
            except Exception as e:
                print('表创建失败:', e)


create_table()
