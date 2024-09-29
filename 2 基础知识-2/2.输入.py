"""
print(): 输出数据
type(): 判断数据的类型
input(): 输入数据
在vs code中使用input不要用code runner执行
"""

# username = input("请输入用户名: ")  # python解释器执行到当前语句会等待用户在终端输入信息
# print(username)
"""
input可以监听用户在键盘上输入的信息并把信息赋值给一个变量
"""
# 任务需求: 让用户输入登录账号和登录密码并在终端打印用户的账号信息

username = input("请输入用户名: ")
password = input("请输入密码: ")
print(f"用户名为: {username}, 密码为: {password}")


"""
input所接收的数据全部都是字符串类型 *
"""
num = input('请输入一个数字: ')
print(num)
print(type(num))

