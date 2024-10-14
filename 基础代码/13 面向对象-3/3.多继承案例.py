# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 20:34
# @Author  : poppies
# @File    : 3.多继承案例.py
# @Software: PyCharm


"""
通过类创建一个手机对象
    1.拍照
    2.玩游戏
    3.打电话
    4.发短信
"""


class Camera:
    def take_photo(self):
        print('拍照功能...')


class PlayGame:
    def play_game(self):
        print('游戏功能...')


class Phone(Camera, PlayGame):
    def call(self):
        print('电话功能...')

    def send_message(self):
        print('短信功能...')


iphone = Phone()
iphone.call()
iphone.send_message()
iphone.play_game()
iphone.take_photo()
