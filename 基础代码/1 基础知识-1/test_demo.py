from lib2to3.pgen2.token import COMMA

b = 20
a = b * 1000
# print((a+1) + "haha活")

print(10 + 33)
print(a + b)
print(20 + 30)
result = 300 + 20
print(result)
result2 = a + b
print(result2)

int_x = 230
float_y = 3.214
str_z = "halopus啊实打实的"
# print("数据类型:" + type(str_z))
print(type(float_y))
print(type(str_z))
print(type(100))
print(type("asdfasfafsda"))
import keyword
print(keyword.kwlist)


print(a + b)
print("int_X的类型是:" , type(int_x))
print('203' + 'sadfads' + '300')
print('100 _ + 200')
print('--------------------------------------')
c = print("int_X的类型是:" , type(int_x))
# print(c)
print(int_x , float_y , str_z)
str_data1 = '小刚今年20岁了'
print(str_data1)
name = '小红'
age = 12.123213234234234123213234234234123213234234234
print('--------------------------------------------------')
str_data2 = '%s今年%d岁啦!' % (name , age )
print(str_data2)
print('int_x类型是: %s!' % (type(int_x)))
type(int_x)
print('______________________________________________')
str_data3 = f'{name}今年{age}岁啦!'
print(str_data3)
str_data3 = '%s今年%d岁啦!' %(name , age)
print(str_data3 ,
      'haha'   
      '========')
str_data4 = '{}今年%d岁啦!!!' .format(name) % (age)
print(str_data4)
str_data4 = '小数是%f' %(age)
print(str_data4)
str_data4 = '小数是%.11f' %(age) #有四舍五入
print(str_data4)
str_data4 = f'小数是{age:.3f}'  #有四舍五入
print(str_data4)
str_data4 = '小数是{:.4f}' .format(age)  #有四舍五入
print(str_data4)


'''
==========我的名片==========
姓名: 顾安老师
email: wt_poppies@sina.com
QQ:xxxxxxx
手机号:172xxxxxx
公司地址:湖南省长沙市xxxx
===========================
'''

name = '哈哈'
email = '1286XXX@163.COM'
qq = '12313xxxxxx'
phonnum = '123213123xxxxx'
add = '江苏南京XXXXXX'

print('===============我的名片=============='
      '\n姓名:%s'
      '\n邮箱:%s'
      '\nQQ:%s'
      '\n手机号:%s'
      '\n公司地址%s'
      '\n===================================='
      %(name , email , qq , phonnum , add))

print(
      '===============我的名片=============='
      f'\n姓名:{name}'
      f'\n邮箱:{email}'
      f'\nQQ:{qq}'
      f'\n手机号:{phonnum}'
      f'\n公司地址{add}'
      '\n===================================='
      )

print(
      '===============我的名片=============='
      '\n姓名:{}'
      '\n邮箱:{}'
      '\nQQ:{}'
      '\n手机号:{}'
      '\n公司地址{}'
      '\n===================================='
      .format(name , email , qq , phonnum , add))