test_list = [1, 2, 3, 4, 4]
test_list[4] = 5
print(test_list)
test_str = '12344'
a = tuple()
test_tuple = ('haha', 'hehe', 'xixi')
new_tuple = test_tuple[1:3]
print(new_tuple)
print(id(a))
print(id(new_tuple))
print(id(1))
print('x' * 30)
test2_tuple = (1, 2, 3, 4, ['haha', 'xixi', 'wo~'])
test2_tuple[4][1] = 'wocao'
print(test2_tuple)
set_1 = set()

test_list = [1, 2, 3, 4, 5, 6]
test_list2 = [11, 22]
test_list.extend(test_list2)
print(test_list)
test_list.append(test_list2)
print(test_list)
print('x' * 33)
set1 = {1, 2, 3, 4, 5, 7}
print(set1)
set1.add(78)
print(set1)
set1.remove(7)
print(set1)
set1.update('11', '12', '33')
print(set1)
a = set1.pop()
print(a, set1)
a = 'bianliang'
set2 = {a, 1, '33', 3.14, (1, 2, 3, 4)}
print(set2)

set1 = {1, 3, 4, 5, 6, 7, 8}
set2 = {7, 8, 10, 11, 12, 13, 14}
print('x' * 88)
print(set1 & set2)
print(set1 | set2)
print(set2 - set1)
print(set1 ^ set2)
a = list(set1)
print(a)
str_data = '我日你妈'
a = set(str_data)
print(a)
b = tuple(str_data)
print(b)

stu_info_dict = {
    'number2':{'username': '张三', 'age': 17, 'class': '502'},
    'number3':{'username': '王五', 'age': 22, 'class': '302'},
    'number4':{'username': '李四', 'age': 24, 'class': '401'},
}
print(stu_info_dict)
print(type(stu_info_dict))
print(stu_info_dict['number2']['username'])
dict1 = {'username': '张三', 'age': 17, 'class': '502'}
for a in dict1:
    print(a)

test_list_dict = [
{'username': '张三', 'age': 17, 'class': '302'},
{'username': '李四', 'age': 22, 'class': '401'},
{'username': '王五', 'age': 23, 'class': '502'},
]
for a in test_list_dict:
    print(a['username'])
111111