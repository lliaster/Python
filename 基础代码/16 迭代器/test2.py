# -*- coding: utf-8 -*-
# @Time     : 2024/10/19 22:14
# @Author   : Lliaster
# @File     : test2.py
import time

class StuDieDai:
    def __init__(self):
        self.index = 0
        self.stu_lst = list()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.stu_lst):
            result = self.stu_lst[self.index]
            self.index += 1
            # time.sleep(1)
            return result
        self.index = 0
        raise StopIteration
    def add_student(self, name,mobile,address):
        self.stu_info=dict()
        self.stu_info['name']=name
        self.stu_info['mobile']=mobile
        self.stu_info['address']=address
        self.stu_lst.append(self.stu_info)


if __name__ == '__main__':
    system_student = StuDieDai()
    system_student.add_student('安娜', 13011111111, '长沙')
    system_student.add_student('双双', 13011111234, '南京')
    system_student.add_student('百川', 13012341234, '北京')
    for i in system_student:
        print(i)

mylst =[{'name': '安娜', 'mobile': 13011111111, 'address': '长沙'},
        {'name': '双双', 'mobile': 13011111234, 'address': '南京'},
        {'name': '百川', 'mobile': 13012341234, 'address': '北京'}]

for i in mylst:
    print(i)