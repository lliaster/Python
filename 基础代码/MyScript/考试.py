# -*- coding: utf-8 -*-
# @Time     : 2024/11/15 22:41
# @Author   : Lliaster
# @File     : 考试.py

print('-----------第一题-------------')
a = [
    'a,1',
    'b,3,22',
    'c,3,4'
]

b = [
    'a,2',
    'b,1',
    'd,2'

]
res = list()
key_list = list()
for item in a + b:
    key_list.append(item[0])
key_list = sorted(set(key_list))

for i in a + b:
    for j in key_list:
        if i.split(',')[0] == j.split(',')[0]:
            key_list[key_list.index(j)] = key_list[key_list.index(j)] + ',' + ','.join(i.split(',')[1::])
print(key_list)

print('---------------第二题------------')

nested_list = [0, [1, 2, 3], [4, 5, [6, 7]], ['123', 8, [9, [10, 11]], 12]]


def listprint(lst):
    for item in lst:
        if isinstance(item, list):
            listprint(item)
        else:
            print(item)


listprint(nested_list)

print('-----------第三题-----------')

lst = [1, 2, 33, 44, 555, 666]

res = dict()
for item in lst:
    print(len(str(item)))
    key = len(str(item))
    if key in res:
        res[key].append(item)
    else:
        res[key] = [item]
    print(res)

print('-----------第四题--------------')

lst = [7, -8, 5, 4, 0, -2, -5]
new_lst = sorted(lst, key=lambda x: (0, x) if x >= 0 else (1, -x))
print(new_lst)

print('-----------第四题2--------------')
new_lst = list()
def sort_key(x):
    if x >= 0:
        return (0, x)
    else:
        return (1, -x)

new_lst2 = list()
for i in lst:
    new_lst2.append(sort_key(i))
print(new_lst2)
new_lst = sorted(new_lst2)
print(new_lst)
# new_lst = sorted(lst, key=sort_key)
# print(new_lst)


