# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 21:45
# @Author  : 顾安
# @File    : 8.__getattribute__代码示例.py


class Person:
    java = 123

    def __getattribute__(self, item):
        print('查询指定的属性或方法是否存在...')
        if item.startswith('h'):
            return 'world'
        else:
            """
            如果使用__getattribute__不要使用self
                __getattribute__遇到实例对象则会被触发
            """
            # return self.set_attribute_method()  # 会出现递归调用
            # return object.__getattribute__(self, item)
            return super().__getattribute__(item)

    def set_attribute_method(self):
        return '模拟设置属性的方法...'


p = Person()
print(p.hello)  # 如果类的内部并没有hello属性则可以使用__getattribute__来创建属性

print(p.java)

p.hello = 123
