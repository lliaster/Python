# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 21:14
# @Author  : 顾安
# @File    : 5.队列的使用


from queue import Queue

# 创建队列对象
# 队列可以设置最大长度
queue = Queue(3)

# 将定义的值上传到队列中
queue.put(1)
queue.put(2)
queue.put(3)

# 如果队列已满, 使用put_nowait会直接抛出异常, 不会造成主线程堵塞
# queue.put_nowait(4)

print('当前队列是否已满:', queue.full())

# queue.put(4)  # 如果队列设置了最大长度, 向上提交超出最大长度的值会造成主线程堵塞

# 获取队列中的一个值
# 队列是先进先出的数据结构

# 获取当前队列中保存的值的个数, 获取一个值, 长度 -1
print('当前队列长度:', queue.qsize())
print(queue.get())
print('当前队列长度:', queue.qsize())
print(queue.get())
print(queue.get())

print('当前队列是否为空:', queue.empty())

# print(queue.get())

# 取值不堵塞直接抛出异常的方法
# print(queue.get_nowait())

# 如果队列中的值被取空了, 那么下一次取值则需要等待队列上传新的值过来
# 会堵塞主线程的执行
# print(queue.get())


"""
get方法和put方法都会造成主线程的堵塞问题
    get: 当队列为空时会发生堵塞
    put: 当队列已满时会发生堵塞
    
判断队列是否已满: full
判断队列是否为空: empty
判断当前队列长度: qsize
上传不等待: put_nowait
获取不等待: get_nowait
"""
