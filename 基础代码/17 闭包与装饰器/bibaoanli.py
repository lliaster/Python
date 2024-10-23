# -*- coding: utf-8 -*-
# @Time     : 2024/10/21 22:03
# @Author   : Lliaster
# @File     : bibaoanli.py


def send_name(name):
    def send_message(message):
        print(name, message)

    return send_message


send_obj = send_name('Lliaster')
send_obj('hello')

print('asdf')
print()
