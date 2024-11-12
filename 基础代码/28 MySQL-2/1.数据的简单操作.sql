-- 数据插入(部分字段插入、全字段插入)
-- 全字段插入
-- insert into <表名> values(<字段1值>, <字段2值>, ...);

-- id自增的情况下可以使用占位符: 0, default, null
insert into students values (0, '安娜', 18, 177.82, '女', 1, 0);
insert into students values (default, '双双', 20, 167.32, '女', 1, 0);
insert into students values (null, '夏洛', 24, 172.33, '男', 2, 0);

-- 部分字段插入
-- insert into <表名>(<字段1>, <字段2>, ...) values(<值1>, <值2>, ...);
insert into students(id, name, height) values (0, '百川', 178.32);

-- 经过测试发现，如果插入的数据没有指定id，那么id会自动增长，不需要使用默认值
-- insert into students(name, height) values ('木木', 166.43);

-- 数据修改
-- update <表名> set <字段名>=<值>, <字段名>=<值>, ... where <条件>;
-- 修改数据是相对比较危险的操作, 所以要加上修改条件, 否则会修改表中所有的数据
update students set height=174.66 where id=3;
update students set height=178.32, cls_id=2 where id=1;

-- 数据删除（逻辑删除）
-- update <表名> set <is_delete>=1 where <条件>;
update students set is_delete=1 where id=3;
select * from students where is_delete=0;

-- 数据删除（物理删除）
-- delete from <表名> where <条件>;
delete from students where id=2;
select * from students;
-- 删除之后再添加新数据则会根据没有删除之前的id值继续自增
insert into students values (default, '小明', 18, 178.32, '男', 1, 0);

-- 数据查询
-- select <字段1>, <字段2>, ... from <表名> where <条件>;  指定字段查询并添加查询条件
-- select * from <表名>;  全字段查询并查询表中的所有数据
-- * 代表所有字段
select * from students;
select name, age, height, gender from students;
select name, age, gender from students where id=1;
