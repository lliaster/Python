list = [1,2,3,4,5]
for i in list:
    if i ==3 :
        continue
    print(i)


def test_value(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test_value(1,2,3,4,5,6,7,8,9,10,name= "test.py",age=18,sex=0,sex_type= "male")

def stu_info(stu_id,stu_name,cls_name):
    print(f'stu_id:{stu_id}\nstu_name:{stu_name}\ncls_name:{cls_name}')

stu_list = [10001,'zhangsan','一班']
stu_info(*stu_list)#拆包


