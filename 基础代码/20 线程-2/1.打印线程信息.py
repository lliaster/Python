# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 20:02
# @Author  : 顾安
# @File    : 1.打印线程信息

import threading
import time


# 只能获取子线程的信息
def work():
    name = threading.current_thread().getName()
    print(name)
    time.sleep(3)


for i in range(5):
    t = threading.Thread(target=work)
    t.setName(f'线程: {i}')
    t.start()

# 获取所有活动线程的信息, 包含主线程
threads = threading.enumerate()
print(threads)

# 打印线程信息
for thread in threads:
    print(f"线程名称: {thread.name}")
    print(f"线程ID: {thread.ident}")
    print(f"是否存活: {thread.is_alive()}")
    print("-" * 20)
