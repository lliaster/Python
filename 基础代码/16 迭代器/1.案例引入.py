# -*- coding: utf-8 -*-
# @Time    : 2024/10/16 20:03
# @Author  : 顾安
# @File    : 1.案例引入


class SystemStudent:
    def __init__(self):
        self.stu_list = list()

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
    # print(system_student.stu_list)

    # 需要从列表中将每一个元素迭代打印
    # for item in system_student.stu_list:
    #     print(item)

    # 直接迭代实例对象本身并获取每个学生的信息
    # for item in system_student:
    #     print(item)

    """
    目前的代码无法直接对实例对象本身进行迭代
        system_student对象不是一个可迭代对象
    """


