from distutils.dep_util import newer

str_data = 'abcdef'
for i in str_data:
    print(i)

print(str_data[1:3])
print(str_data[:3])
# float_data = 3.12312
# for i in float_data:
#     print(i)

print(str_data[2:5])
print(str_data[:4:3])
print('-' * 88)
print(str_data[1:-1])
print(str_data[1:])
print(str_data[::-1])
print(str_data[-1:3:-1])
print('-' * 88)
print(str_data[::])

s = 'hello whord'
print(s[::-1])

# find
str1 = 'hello to this city'
print(str1.find('to'))
print(str1.rfind('to'))
# count 统计
print(str1.count('t'))
# replace 替换
print(str1.replace('h', '2', 1))
# split  切割
print(str1.split('t'))
print(str1.split(' ')[::-1])
# startswih 开头判断
a = str1.split(' ')[-1]
print(a.startswith('c'))
print(str1.split(' ')[1])
print(str1.split(' ')[1].startswith('c'))
print('-' * 99)
print(str1.split(' ')[1])
b = str1.split(' ')[1]
print(str1.replace(b,'of'))
# upper
print(str1.upper())

#strip
print(str1.strip())
print(str1.replace(' ',''))

a = 'asdfasdf'
b = 'qwer'
c = '213213'
print(a.join(a).join(c),'-',)

print('- '*55)
print(a[::])

list1 = ['1','2','3','4']
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print(list1)
print('1111111111111111')

del list1[1]
print(list1)

list1 = ['1','2','3','4']
list2= ['1,11,111,1111zhangsan']
a = list1.append('haha')
print(a)
