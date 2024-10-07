name_lst = ['张三','李四','王五']
gender_lst = ['男','女','男']

def print_student_info(name, gender):
    print(f'学生姓名: {name}, 学生性别: {gender}')

for i in zip(name_lst, gender_lst):
    print(i)
    print_student_info(*i)
