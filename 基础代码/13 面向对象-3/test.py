class A:
    def run_a(self):
        print('这是类A中的run方法')

    def run(self):
        print('这是类A中的run方法')


class B:
    def run_b(self):
        print('这是类B中的run方法')

    def run(self):
        print('这是类B中的run方法')


# 类C可以获取不同的父类中的资源
class C(A, B):
    pass

c = C()
c