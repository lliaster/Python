print('今天\n星期5')

print(r'哈哈哈\nn')
print('几级啊士大夫\t123213123211\n1232\t撒旦发顺丰的')
print('--------------------------')
# username = input('请输入用户名:     ')
# print(username)

username = input('请输入用户名:   ')
userpassword = input('请输入用户密码:  ')
print('占位符表达式:'
    '用户名是:[%s]\n用户密码是:[%s]' % (username, userpassword))
print('用户名是:%s\n用户密码是:%s' % (username, userpassword))
print('=================================================================')
print('f表达式:'
      f'用户名是:{username} \n用户密码是{userpassword}'
      '\n===================================================================')
print('format表达式:'
      '\n用户名是:{} \n用户密码是:{} '
      '\n=================================='.format(username, userpassword))
print(type(username))

