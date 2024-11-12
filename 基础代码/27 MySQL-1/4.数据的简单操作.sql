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

