-- 视图类似python中的函数, 将一个复杂的查询语句封装成一个类似于函数名的视图
use python_test_1;

select 城市信息.* from tb_areas as 城市信息
    inner join tb_areas as 省份信息 on 城市信息.pid=省份信息.aid where 省份信息.atitle='广东省';


-- 创建视图
create view v_city_info as select 城市信息.* from tb_areas as 城市信息
    inner join tb_areas as 省份信息 on 城市信息.pid=省份信息.aid where 省份信息.atitle='广东省';

-- 查询创建的视图
show tables;

-- 执行视图
select * from v_city_info;

-- 删除视图
drop view v_city_info;