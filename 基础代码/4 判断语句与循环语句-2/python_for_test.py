from encodings.idna import Codec
from itertools import count

from idna.intranges import intranges_from_list
from selenium.webdriver.common.devtools.v85.dom_storage import remove_dom_storage_item
from unicodedata import numeric

liebiao = [1,23,14,123,45,]
print(liebiao)
for haha in liebiao:
    print(haha, end=' ')

zifu = '12314'
for haha in zifu:
    print(haha, end=' ')


print('\n============================')
for i in range(3,5):
    print(i, end=' ')
a = range(0,1000,100)
print('====================')
print(list(a))


b = range(1000, 1 , -100)
print(list(b))

c = 0
for s in  range(101):
    c += s
print(c)

a = 0
c = 0
while a <= 100:
    c += a
    a += 1
print(c)

int_list = range(10)
num = 3

print(num in int_list)
print('======================')
for it in int_list:
    print(it)
    if it == num:
        break

for s in range(10):
    if s == 6:
        continue
    else:
        print(f'当前值{s}')

username = 'admin'
userpass = '123'

# for s in range(3, 0 , -1):
#     user = input('请输入用户账号:')
#     password = input('请输入用户密码:')
#     if user == username and password == password:
#         print('登录成功')
#         break
#     elif s == 0:
#         print('账号锁定')
#         break
#     else:
#         print(f'登录失败当前次数为{s -1}')

x = 0
while x < 3:
    x = x + 1
print(x)


num = 0
while num<=3:
    print(num)
    num = num + 1


x = 10
while x > 5:
    x = x - 1
    print(x)

for s in range(11):
    if s < 10:
        continue
    print(s)
print('x' * 30)

for s in range(0, 3 ,-1):
    print(s)

