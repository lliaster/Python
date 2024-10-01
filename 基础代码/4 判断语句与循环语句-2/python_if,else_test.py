age = 17
xianzhi = 18
print('if代码即将被执行')

if age >= xianzhi:
    print('已经成年'
          '\n可以去干活了'
          '\n可以去上网了')
else:
    print(f'你还没有{xianzhi}岁'
          '\n你还没有%d岁哦,加油哦' % xianzhi)


# local_name = 'admin'
# local_password = '123456'
#
# username = input('请输入用户名:')
# password = str(input('请输入密码:'))
#
# if username == local_name and password == local_password:
#     print('登录成功')
# else:
#     print('登录失败')
#



'''
if 嵌套判断

'''
print('===============================')
anjian = True
gaotiepiao = True

if anjian == True :
    print('安检通过')
    if gaotiepiao:
        print('有票可以上车')
    else:
        print('没票不给上策划')
else:
    print('安检没通过')

print('===============================')
print('===============================')

score = 45
print(type(score))
if 100 >= score >= 90:
    print('牛逼')
elif 90 > score >= 80:
    print('可以啊')
elif score < 80 and score >= 70:
    print('不错')
elif score < 70:
    print('啊??????')
else:
    print('分数输入有误')



