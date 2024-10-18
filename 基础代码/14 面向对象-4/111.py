class Mycalss:
    def __init__(self):
        self.__x=10
        self.y=20
obj = Mycalss()
print(obj.y)


class MyClass:
    @staticmethod
    def static_method():
        return "jintai"

    @classmethod
    def class_method(cls):
        return "class"
print(MyClass.static_method())
print(MyClass.class_method())