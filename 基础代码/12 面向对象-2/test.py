class Animal:
    def eat(self):
        print('正在进食...')

    def drink(self):
        print('正在喝水...')

    def __run(self):
        print('正在奔跑...')

    def run_method(self):
        self.__run()

    def info(self):
        print('这是父类中的info方法...')


class Dog(Animal):
    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age

    def dog_info(self):
        print(self.dog_name, self.dog_age)


dog1 = Dog('haha', 17)

# dog1.eat()
#


class Person:
    def eat(self):
        print('吃饭')
    def run(self):
        print('跑')
    def drink(self):
        print('喝水')

class FlasePerson(Person):
    def __init__(self):
        pass
    def eat(self):
        print('子类吃')
    def look(self):
        print('看')
    def fathr_eat(self):
        Person.eat(self)

jiaren = FlasePerson()
jiaren.eat()
jiaren.drink()
jiaren.fathreat()
