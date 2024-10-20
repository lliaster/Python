# -*- coding: utf-8 -*-
# @Time     : 2024/10/19 22:55
# @Author   : Lliaster
# @File     : test4.py
import time
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
t1= time.time()

print([i for i in range(0,10000000)])
t2 = time.time()
print(f'耗时：{round(t2-t1,3)}s' )