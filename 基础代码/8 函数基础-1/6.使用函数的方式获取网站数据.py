# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 21:08
# @Author  : poppies
# @File    : 6.使用函数的方式获取网站数据.py
# @Software: PyCharm


# python这门语言已经提供了爬虫的工具: requests
# 需要大家去下载安装: pip install requests
# pip install urllib3==1.26.18

# 将下载安装好的第三方模块导入到当前文件
import requests


# 定义一个函数, 让这个函数可以访问到网站并获取网站的页面数据
def get_info(url):
    response = requests.get(url)
    # 打印请求网站成功后返回的页面信息
    print(response.content.decode())


url_1 = 'https://www.baidu.com/'
get_info(url_1)

url_2 = 'https://www.bing.com'
get_info(url_2)



