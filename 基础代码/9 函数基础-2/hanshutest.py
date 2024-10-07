def work_1():
    print(1)


def work_2():
    work_1()
    print(2)


work_2()


def work():
    num = 3


def xuxian(a):
    print('-' * a)


xuxian(60)


def cixuxian5cixuxian(num):
    i = 0
    while i < num:
        xuxian(40)
        i += 1
cixuxian5cixuxian(5)


def tree_int_sum(a,b,c):
    print(f'三个数和是:{a+b+c}')
    return a+b+c
def avg_three_int_sum(a,b,c):
    res =tree_int_sum(a,b,c)
    print(f'三个数平均值是:{res/3:.2f}')



# print(TreeIntSum(1, 3, 5))
avg_three_int_sum(1,3,5)
