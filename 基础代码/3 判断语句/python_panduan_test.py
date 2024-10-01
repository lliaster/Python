T = True
F = False
print(T)
print(type(T))


age = 18
if age < 18:
    print(T)
else:
    print(F)
print('============================')
num1 = 10
num2 = 20
print(num1 > num2)
print(num2 > num1)
print(num1 == num2 ,
      '\n=====================')

num1 = 20
print(num1 >= num2)
print(num1 <= num2)
print('123213' == '123213')

print('=================逻辑运算符==================')
print(100 > 50 and 90 <100)
print(100 == 50 and 90 <100)
print(100 == 50 or 90 == 100)
print(100 == 50 or 90 <100)


#not 取反
print('==================取反================')
print(not 10 > 9)
print(not (100 > 50 and 90 <100))
print(not (100 > 50 or 90 <100))

print('=========================')
print(100 and 100)
print(110 and 1)
print(100 and 110)  #
print(100 or 100)
print(0 or 1)
print(0 and 3)
print(3 and 0)
print(100 and 100>5)
'''
底层问题,其实是从左到右的判断, and中 如果 最左侧是 空值 对象 则不运行后续的值
如果左侧的值 不是空对象 则顺序运行
'''

print('=============列表============')
int_list = []
if int_list:
    print(1)
else:
    print(2)


print('===================作业===================='
      '\n=============or===============')

print(100 or 200)  # 输出什么呢？   100
print(100 or 100>50)  # 输出什么呢？  100
print(0 or 200)  # 输出什么呢？     0
print(0 or 100>50)  # 输出什么呢？     0         or的关系是两个中间通过一个  则返回 有值的

print('===================and ===============')
print(100 and 200)  # 输出什么呢？   200
print(100 and 100 > 50)  # 输出什么呢？   True
print(0 and 200)  # 输出什么呢？      0
print(0 and 100 > 50)  # 输出什么呢？  0
print(200 and 0)  # 输出什么呢？      0
print(100 > 50 and  0)  # 输出什么呢？  0
print('============复合==========')
print(0 or 100>50 or 0 ) #  T
print( 0 and 100>50 or 0)     #0
print( 0 or 100>50 and 0)  #0
print( 0 or 100>50 and 3)   #3
print( 0 or (100>50 and 0)) #0
print( 0 or (100>50 and 3)) #3
print('============测试===============')
print(0 or 1 and 3)  #3
print(0 or (1 and 0))  #0
print(0 and 3 and 3)   #0
print(0 and 1 or 3)    #3
print(0 or 1>4 and 3)   #f
print(4>6 and 7>4 or 3<4)  #t
print(4>6 and 7>4 or 3)  #3
print((3 or  4>6) and 7>4)  #T
print(3 or 4 or 4>6 and 7>4)  #3
print( 3 and  False and 4 )#f
print( 3 and  True or 4 )#t
print( 3 and  False or 4 )#4
print('============测试===============')
print('============测试===============')
print( 3 or True )#4