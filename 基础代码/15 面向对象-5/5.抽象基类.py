# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 21:34
# @Author  : 顾安
# @File    : 5.抽象基类


"""
抽象基类是其他子类的一个模板, 抽象基类本身不能被实例化
"""
from abc import ABC, abstractmethod


# 模拟开发一个框架: 爬虫框架
# 框架一般都是通用性的, 在遇到一些特殊情况需要重写框架中的方法
class MySpider(ABC):
    @abstractmethod
    def get(self):
        pass

    def post(self):
        pass

    def options(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class BaiDuSpider(MySpider):
    def get(self):  # 子类必须重写抽象基类中被装饰的方法: abstractmethod
        pass


baidu = BaiDuSpider()


"""
父类如果是一个抽象基类, 子类继承父类必须重写被abstractmethod装饰的方法, 哪怕不调用也要重写
"""
