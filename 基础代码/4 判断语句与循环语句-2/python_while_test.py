'''
a = 0
while a < 10000:
    print('哈哈哈', a )
    a += 1
'''

# i = 1
# while i <= 5:
#     print(i,'哈哈哈%d' % i )
#     i = i+1
'''
i = 0
t = 0
while i <= 100:
    t = i + t
    i = i + 1
    print('当前循环%d次,最后的当前相加的和是%d'
          '\n=============' % (i , t))
'''
# i = 0
# t = 0
# while i < 100:
#     if i % 2 == 0:
#         t += i
#     else:
#         pass
#     i += 1
#     print('当前循环%d次,最后的当前相加的和是%d' % (i , t))

    # 1 0
    # 2 2
    # 3 2
    # 4 6
# i = 1
# c = 0
# while i < 100:
#     if i % 3 == 0:
#         c += i
#     elif i % 7 == 0:
#         c += i
#     print('当前数字是%d,相加的和是%d' % (i, c))
#     i += 1


# i = 1
# c = 0
# while i < 100:
#     if i % 3 == 0 and i % 7 == 0:
#         c += i
#     print('当前数字是%d,相加的和是%d' % (i, c))
#     i += 1


# s = 6
# row = 1
# while row <= s:
#     strs = '*' * row
#     row += 1
#     print(strs)
#
# print('==========================', end= '阿道夫')
# print()
#
#
# kuan = 5
# gao = 1
# while gao <= kuan:
#     shijikuan = 1
#     while shijikuan <= gao:
#         print('*' , end='  ')
#         shijikuan += 1
#     gao += 1
#     print()
# print(1111)
# print(213123 , end ='   ')


'''九九乘法表'''

kuan = 9
gao = 1
while gao <= kuan:
    shijikuan = 1
    qiankongge = 1
    print(f'{(kuan - gao) * "      "}' ,end='')
    while shijikuan <= gao:
        print(f'{gao} X {shijikuan} = {gao * shijikuan}' , end='    ')
        shijikuan += 1
    gao += 1
    print()
#
# kuan = 9
# gao = 1
# while gao <= kuan:
#     print(kuan * 'A')
#     gao += 1
#
# kuan = 9
# gao = 1
# while gao < kuan:
#     shijikuan = 1
#     while shijikuan < kuan:
#         print(shijikuan * 'a')
#         shijikuan += 1
#         gao += 1
#
#



