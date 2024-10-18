# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 21:13
# @Author  : 顾安
# @File    : 7.完成对学生信息的迭代

import time


class SystemStudent:
    def __init__(self):
        self.index = 0
        self.stu_list = list()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.stu_list):
            result = self.stu_list[self.index]
            self.index += 1
            time.sleep(1)
            return result
        else:
            self.index = 0
            raise StopIteration

    def add_student(self, name, mobile, address):
        stu_info = dict()
        stu_info['stu_name'] = name
        stu_info['stu_mobile'] = mobile
        stu_info['stu_address'] = address
        self.stu_list.append(stu_info)


if __name__ == '__main__':
    system_student = SystemStudent()
    system_student.add_student('安娜', 13011111111, '长沙')
    system_student.add_student('双双', 13011111234, '南京')
    system_student.add_student('百川', 13012341234, '北京')

    for temp in system_student:
        print(temp)

"""
关于迭代器对象的实现主要在一个类的内部实现两个特殊的魔术方法:
    __iter__方法与__next__方法
"""
