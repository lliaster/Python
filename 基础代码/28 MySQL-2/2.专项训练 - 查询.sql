show databases;
use python_test_1;

-- drop table classes;
-- drop table students;


-- students表
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

-- classes表
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);

-- 向students表中插入数据
insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,NULL,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0);

-- 向classes表中插入数据
insert into classes values (0, "python_01期"), (0, "python_02期");

-- 数据查询
select * from students;
select name, gender from students;

-- 设置别名
select id as 学生编号, name as 学生姓名, gender as 学生性别 from students;
select 学生表.id as 学生编号, 学生表.name as 学生姓名, 学生表.gender as 学生性别 from students as 学生表;


-- 数据去重(不是修改表数据, 返回的结果带有去重效果)
-- select distinct <字段1>, <字段2> from <表名>;
select gender from students;
select distinct gender from students;


-- 运算符
select * from students where id < 5;
select * from students where id > 5;
select * from students where id <= 5;
select * from students where age >= 18;

select * from students where id != 4;
select * from students where id <> 4;


-- 逻辑运算
select * from students where id > 3 and gender='女';
select * from students where id > 3 or gender='女';
select * from students where not gender='女';


-- 模糊查询
-- select <字段1>, <字段2>, ... from <表名> where <字段> like < 值<% 或 _> >;
-- select * from students;
-- %: 任意个数字符
select * from students where name like '黄%';
select * from students where name like '周%';
select * from students where name like '周_';
select * from students where name like '周__';

-- 范围查询
-- 非连续范围
-- select <字段1>, <字段2>, ... from <表名> where <字段> in (<值1>, <值2>, ...);
select * from students where name in ('黄蓉', '周杰', '周杰伦');

-- 连续范围
-- select <字段1>, <字段2>, ... from <表名> where <字段> between <值1> and <值2>;
select * from students where id between 1 and 6;
select * from students where (id between 1 and 6) and gender='女';


-- 空判断
select * from students where height is null;
select * from students where height is not null;
-- select * from students where height=null; 判断空不能用等号


-- 排序
-- select <字段1>, <字段2>, ... from <表名> order by <字段1> <asc/desc>, <字段2> <asc/desc>, ...;
select * from students order by id desc;
-- select * from students order by id asc;

select * from students order by age desc, id desc;


-- 聚合函数
select count(*) as 学生总数 from students;
select max(age) as 最大年龄 from students;
select min(age) as 最小年龄 from students;
select sum(age) as 总年龄 from students;
select avg(age) as 平均年龄 from students;


-- 分组查询
-- select <字段1>, <字段2>, ... from <表名> group by <字段1>, <字段2>, ...;
-- select gender from students group by gender;
select gender as 学生性别, group_concat(name) as 学生姓名 from students group by gender;
select gender as 学生性别, group_concat(id) as 学生编号 from students group by gender;
select gender, count(*) from students group by gender;
select gender, avg(age) from students group by gender;

-- 在分组之后筛选需要使用having
select gender, count(*) from students group by gender having count(*) > 1;


-- 分页查询
-- select <字段1>, <字段2>, ... from <表名> limit <开始索引>, <查询数量>;
select * from students limit 0, 2;
select * from students limit 2;

select * from students limit 0, 5;
select * from students limit 9, 5;

-- 开始索引+1, 如果条数不够则返回当前表中的最后一条
select * from students limit 11, 5;


-- 链接查询
-- select <字段1>, <字段2>, ... from <表1> inner join <表2> on <表1>.<字段1>=<表2>.<字段2>;
-- 内链接
select * from students inner join classes on students.cls_id=classes.id;
-- 左链接
select * from students as 学生表 left join classes as 班级表 on 学生表.cls_id=班级表.id;
select * from classes as 班级表 left join students as 学生表 on 学生表.cls_id=班级表.id;
-- 右链接
select * from students as 学生表 right join classes as 班级表 on 学生表.cls_id=班级表.id;


-- 自关联查询
create table tb_areas(
    aid int primary key,
    atitle varchar(20),
    pid int
);

-- select * from tb_areas;
select * from tb_areas where pid is null;
select * from tb_areas where atitle='湖南省';
select * from tb_areas where atitle='长沙市';
select * from tb_areas where aid=430000;

select 城市信息.* from tb_areas as 城市信息
    inner join tb_areas as 省份信息 on 城市信息.pid=省份信息.aid where 省份信息.atitle='广东省';

select 区县信息.* from tb_areas as 区县信息
    inner join tb_areas as 城市信息 on 区县信息.pid=城市信息.aid where 城市信息.atitle='长沙市';


-- 子查询: 查询效率不高
select avg(age) from students;
select * from students where age > 27.6429;
select * from students where age > (select avg(age) from students);

select * from students where cls_id in (select id from classes where name='python_01期');
select * from students where cls_id in (select id from classes where name='python_02期');