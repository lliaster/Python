def work_1():
    print(1)


def work_2():
    print(2)
    # 在work_2函数内部调用work_1
    work_1()


work_2()
