# -*- coding: utf-8 -*-
# @Time    : 2024/10/28 21:28
# @Author  : 顾安
# @File    : 6.在不获取任务返回值的情况下让主线程堵塞.py


from concurrent.futures import ThreadPoolExecutor, wait

url = 'https://movie.douban.com/top250?start={}&filter='


def get_movie_info(movie_url):
    print(f'当前爬取的地址为: {movie_url}')
    # time.sleep(randint(1, 2))


# 1.创建线程池对象
pool = ThreadPoolExecutor()

# 2.提交任务
future_list = [pool.submit(get_movie_info, url.format(page * 25)) for page in range(10)]

# 3.让主线程堵塞, 接收的是future对象列表, 不能传递单个future对象
wait(future_list)

# 4.程序结束
print('主程序结束...')

# 5.释放线程池对象
pool.shutdown()
