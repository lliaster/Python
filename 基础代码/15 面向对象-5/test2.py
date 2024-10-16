class Person:
    def __del__(self):
        print('代码即将推出')

    def test_fangfa1(self):
        print("Test1")



obj = Person    #为啥变成参数
obj()         #为啥还能调用的
obj2 = obj()

'''
Person 类定义了两个方法：__del__ 和 test_fangfa1。
__del__ 是析构方法，在对象被销毁时调用，打印“代码即将推出”。
test_fangfa1 方法打印“Test1”。
代码解释：
obj = Person：将 Person 类赋值给 obj，此时 obj 是类本身。
obj()：调用 Person 类的构造函数，创建一个 Person 对象并立即销毁，触发 __del__ 方法。
obj = Person()：创建一个 Person 对象，并将其赋值给 obj，此时 obj 是一个实例对象
'''


class Student:
    def __call__(self, *args, **kwargs):
        print('我被触发了')

student = Student()
student()


print(Student.__dict__)




