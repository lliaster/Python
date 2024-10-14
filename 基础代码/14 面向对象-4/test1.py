class A:
    num = 10
    def get_attr(self):
        print(self.num)
        print(A.num)
a =A()
a.get_attr()

class Person:
    gender = '男'
    def __init__(self, name):
        self.name = name
    @staticmethod
    def info(canshu_obj):
        print('这是一个静态方法')
        print(canshu_obj.gender, canshu_obj.name)
    def self_info(self):
        print('这是一个实例方法...')
        print(f'姓名是:{self.name},性别是:{self.gender}')

person = Person('张三')
person.info(person)
# Person.info()