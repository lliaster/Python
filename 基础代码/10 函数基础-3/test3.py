def test_methods():
    print('测试函数')
def work(func_obj):
    def wapper():
        func_obj()
    return wapper
wra_func=work(test_methods)
wra_func()



stus = [
    {"name": "顾安", "age": 18},
    {"name": "夏洛", "age": 19},
    {"name": "木木", "age": 17}
]


def stu_age(item):
    return item['age']

stus.sort(key = stu_age)
print(stus)

stus.sort(key=lambda item:item['age'])


# def test.py():
#     print('这是一个递归函数')
#     test.py()
# test.py()
a=range(2,10)
print(a)