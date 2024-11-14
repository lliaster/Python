# -*- coding: utf-8 -*-
# @Time     : 2024/11/15 22:05
# @Author   : Lliaster
# @File     : test.py

lst = [1, 2, 3, 4, 5]
new_lst = [i * i for i in lst]
print(new_lst)




def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper


@my_decorator
def str_print():
    print("Hello, world!")

str_print()



def func(n):
    if n <2:
        return n
    return  func(n-1) + func(n-2)
print(func(5))



def gen ():
    yield from range(3)
    yield from range(4,7)

for i in gen():
    print(i)

nested_list = [
    [1, 2, 3],
    [4, 5, [6, 7]],
    [8, [9, [10, 11]], 12]
]