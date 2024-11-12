-- 新建数据库
-- create database <数据库名称> charset=<字符集>;
-- create database python_basic charset=utf8;

-- 查看数据库
show databases;

-- 进入数据库
use python_basic;

-- 查看当前数据库下所有表
show tables;

-- 创建表
-- auto_increment: 自增长(插入一条数据id自动加1, 默认从1开始)
-- unsigned: 无符号
-- 字段与字段之间通过逗号分割
-- 最后一个字段不能加逗号
create table stu_info(
    id int primary key auto_increment,
    name varchar(10) not null,
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男', '女', '未知', '塑料袋'),
    cls_id int unsigned default 1
);

-- 创建班级表
create table cls_info(
    id int primary key auto_increment,
    cls_name varchar(10) not null
);

-- 查询表结构
-- desc <表名>;
desc stu_info;

-- 添加新字段
-- alter table <表名> add <字段名> <字段类型> <约束>;
alter table stu_info add birthday datetime;

-- 修改字段(修改字段名称并根据业务场景添加约束)
-- alter table <表名> change <原有字段名称> <新字段名称> <字段类型> <约束>;
alter table stu_info change birthday birth date not null;

-- 修改字段(保持原有字段名称的情况下修改字段类型或者约束)
alter table stu_info modify birth datetime;

-- 删除字段: 慎用
-- alter table <表名> drop <字段名>;
-- alter table stu_info drop birth;

-- 删除表: 慎用
-- drop table <表名>;
-- drop table cls_info;

-- 查询指定表的创建过程
-- show create table <表名>;
show create table stu_info;


