# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 20:40
# @Author  : poppies
# @File    : 4.学生管理系统 - 函数版本.py
# @Software: PyCharm


"""
1.要打印当前系统的操作菜单
2.添加学生
3.删除学生
4.修改学生
5.查询指定的一个学生
6.查询所有学生
7.系统退出功能
"""

info_list = list()


def print_menu():
    print('')
    print("*" * 27)
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("*" * 27)
    print('')


def add_new_info():
    """添加学生信息"""
    new_name = input('请输入姓名:')
    new_tel = input('请输入手机号:')
    new_qq = input('请输入QQ:')

    # 创建学生id
    new_id = len(info_list) + 1

    # 判断新加入的学生是否已经存在
    for temp_info in info_list:
        if temp_info['id'] == new_id:
            print('当前学号已存在, 请勿重复添加...')
            return

    # 将上面的信息汇总成一个字典数据作为存储
    info = dict()
    info['id'] = new_id
    info['name'] = new_name
    info['tel'] = new_tel
    info['qq'] = new_qq

    # 将一个学生的字典信息添加到列表中
    info_list.append(info)
    print(info_list)


def del_info():
    """删除学生信息"""
    del_num = int(input('请输入你要删除的学生序号:'))

    # 序号从1开始, 列表索引是从0开始, 所以需要对用户输入的序号 - 1
    index = del_num - 1

    # 判断用户输入的列表索引是否存在
    if 0 <= index <= len(info_list):
        del_flag = input('是否删除: y or n')
        if del_flag == 'y':
            del info_list[index]
    else:
        print('序号输入有误, 请重新输入...')


def modify_info():
    """修改学生信息"""
    nodify_num = int(input('请输入你要修改的学生序号:'))

    index = nodify_num - 1
    if 0 <= index <= len(info_list):
        print('你要修改的学生信息为:')
        info = info_list[index]
        print("学号:%s, 姓名:%s, 手机号:%s, QQ:%s" % (info['id'], info['name'], info['tel'], info['qq']))

        new_name = input('请输入姓名:')
        new_tel = input('请输入手机号:')
        new_qq = input('请输入QQ:')

        # 更新学生信息
        info['name'] = new_name
        info['tel'] = new_tel
        info['qq'] = new_qq
    else:
        print('序号输入有误, 请重新输入...')


def search_info():
    """查询一位学生的信息"""
    search_name = input('请输入你要查询的学生姓名:')

    for temp_info in info_list:
        if temp_info['name'] == search_name:
            print('查询的学生信息如下:')
            print("学号:%s, 姓名:%s, 手机号:%s, QQ:%s" % (
                temp_info['id'], temp_info['name'], temp_info['tel'], temp_info['qq']))
            break
    else:
        print('暂无学生信息...')


def search_all_info():
    print("序号\t\t学号\t\t姓名\t\t手机号\t\t\tQQ")
    i = 1

    for temp_info in info_list:
        print('-' * 47)
        print("%d\t\t%s\t\t%s\t\t%s\t\t%s" % (i, temp_info['id'], temp_info['name'], temp_info['tel'], temp_info['qq']))
        i += 1


def main():
    while True:
        print_menu()
        option = input("请选择操作:")

        # 分支操作
        if option == '1':
            add_new_info()
        elif option == '2':
            del_info()
        elif option == '3':
            modify_info()
        elif option == '4':
            search_info()
        elif option == '5':
            search_all_info()
        elif option == '6':
            print("感谢使用学生管理系统，再见！")
            break
        else:
            print("输入有误，请重新输入...")


main()
