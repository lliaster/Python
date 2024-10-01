from audioop import reverse
from tkinter.font import names

a_list = [8,2,1,3,4,5]
# a_list.sort(reverse=True)
# print(a_list)
# a_list.reverse()
# print(a_list)

print(sorted(a_list))

b = a_list.sort()
print(a_list,b)


school_names = [
    ['北京大学', '清华大学'],
    ['南开大学', '天津大学', '天津师范大学'],
    ['山东大学', '中国海洋大学']
]
print(school_names[1][0])
school_names.insert(0,['hello','ada'])
print(school_names)
print(school_names[3][0])
import random
zuowei = [[],[],[]]
names = ['a','b','c','d','e','f','g','h']
for name in names:
    zuowei_bianhao = random.randint(0,2)
    zuowei[zuowei_bianhao].append(name)
    print(f'当前办公室编号:{zuowei_bianhao},'
          f'人数{len(zuowei[zuowei_bianhao])},'
          f'分别是{zuowei[zuowei_bianhao]}')
print(f'当前办公室分配如下{zuowei}')
dangqian_num = 1
for a in zuowei:
    print(f'当前办公室编号为:{dangqian_num},人数为{len(a)}')
    dangqian_num += 1
    # print(a)
    c = ','.join(a)
    print(f'里面的老师分别是:{c}')
    print('里面的老师分别是:',end='')
    for b in a:
        print(f'{b}',end='')
    print()

