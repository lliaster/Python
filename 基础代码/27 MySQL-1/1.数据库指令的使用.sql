-- 链接数据库: 输入指令后还需要输入数据库密码
-- mysql -uroot -p

-- 查看数据库
show databases;

-- 进入指定数据库之下
-- use <数据库名称>;
use mysql;

-- 查询指定数据库之下的所有的数据表
show tables;

-- 查询当前位于哪个数据库之下
select database();

-- 查询MySQL版本: 不常用
select version();

-- 创建一个自定义数据库
-- create database <数据库名称> charset=<字符集>;
create database python_basic charset=utf8;

-- 删除数据库: 慎用
-- drop database <数据库名称>;
# drop database python_basic;
