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
info_list = [{'id': 1, 'name': 'zhangsan', 'tel': '12345677', 'qq': '123456'},
             {'id': 2, 'name': 'lisi', 'tel': '12345677', 'qq': '12345687'}]


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

    # 判断添加的学生信息是否存在
    for stu_info in info_list:
        if stu_info['id'] == new_name:
            print('当前学号已存在, 请勿重复添加...')
            return
    # 汇总学生信息 为一个字典数据
    info = dict()
    info['id'] = new_id
    info['name'] = new_name
    info['tel'] = new_tel
    info['qq'] = new_qq
    info_list.append(info)
    print(f'当前学生信息为:{info}\n所有学生信息如下:\n{info_list}')


def del_info():
    """删除学生信息"""
    del_num = int(input('请输入你要删除的学生序号:'))
    shanchuxuhao = del_num - 1
    if 0 <= shanchuxuhao <= len(info_list):
        del_flag = input('是否删除: y or n')
        if del_flag == 'y':
            del info_list[shanchuxuhao]
        else:
            print('输入有误, 请重新输入...')


def modify_info():
    """修改学生信息"""
    nodify_num = int(input('请输入你要删除的学生序号:'))
    xuehao_num = nodify_num - 1
    if 0 <= nodify_num <= len(info_list):
        print('你要修改的学生信息为:')
        info = info_list[xuehao_num]
        print("学号:%s, 姓名:%s, 手机号:%s,  qq:%s" % (info['id'], info['name'], info['tel'], info['qq']))
        new_name = str(input('请输入姓名:'))
        new_tel = str(input('请输入手机号:'))
        new_qq = str(input('请输入QQ:'))
        print(f'当前学生信息为:{info}\n所有学生信息如下:\n{info_list}')
        info['name'] = new_name
        info['tel'] = new_tel
        info['qq'] = new_qq
    else:
        print('序号输入有误, 请重新输入...')


def search_info():
    """查询一位学生的信息"""
    sheach_name = input('请输入学生姓名:')
    for temp_info in info_list:
        if temp_info['name'] == sheach_name:
            print('当前查询学生信息如下')
            print('学号:%s,姓名:%s,手机号:%s,qq号:%s' % (
                temp_info['id'], temp_info['name'], temp_info['tel'], temp_info['qq']))
            break
        else:
            print('暂无学生信息...')

def search_all_info():
    print('学号\t\t姓名\t\t\t\t手机号\t\t\tqq号\t\t')
    for temp_info in info_list:
        print('-'*47)
        print('%s\t\t%s\t\t%s\t\t%s\t\t'%(temp_info['id'],temp_info['name'],temp_info['tel'],temp_info['qq']))


search_all_info()

# print(info_list)
search_info()
# print_menu()
# add_new_info()
