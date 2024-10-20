# -*- coding: utf-8 -*-
# @Time    : 2024/10/18 20:01
# @Author  : 顾安
# @File    : 1.回顾 - 生成器中的内置方法


def my_range(n):
    i = 0
    while i < n:
        value = yield i
        if value:
            print('这是yield获取的值:', value)
        else:
            print('发送的信号为False')
        i += 1


obj = my_range(5)
print(next(obj))
print(next(obj))

# 生成器对象.send(value): send方法可以将一个值发送给yield关键字并将这个值赋值给一个变量
# send方法也具有驱动生成器对象的功能, 与next类似
# 通过send发送的数据其实是一个信号, 根据信号的不同可以让生成器返回不同的结果/操作不同的代码
print(obj.send(False))

print(next(obj))  # 当前代码是从赋值开始往下执行

# send方法使用的注意点
# 如果生成器是第一次执行则不要直接使用send去驱动生成器, 如果需要第一次使用send驱动则传递的值必须是None
# 必须已经驱动过一次生成器之后才能用send方法
# print(obj.send(None))


# close: 用于关闭生成器
obj.close()  # 类似与在循环中使用的break
print(next(obj))




