# 就是python提供的一个变量, 变量内部又提供了一些可以被执行的方法
# 如果一个对象可以被循环执行, 那么这个对象就是一个迭代对象

int_list = [1, 2, 3, 4, 5]  # 迭代的将列表中的元素依次打印出来
for i in int_list:
    print(i)


# 字符串也是一种迭代对象
str_data = "hello world"
for i in str_data:
    print(i)


# 哪些对象不能被循环执行
# float_data = 3.14
# for i in float_data:
#     print(i)

