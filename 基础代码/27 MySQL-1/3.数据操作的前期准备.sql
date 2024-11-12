-- 新建测试数据库
create database python_test_1 charset=utf8mb4;

-- 切入测试数据库
use python_test_1;

-- 创建测试表(学生表、班级表)
create table students(
    id int primary key auto_increment,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女', '中性', '保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

create table classes(
    id int primary key auto_increment,
    name varchar(30) not null
);


-- 查询表结构
desc students;
desc classes;
