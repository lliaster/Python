# -*- coding: utf-8 -*-
# @Time     : 2024/10/24 16:04
# @Author   : Lliaster
# @File     : kanbudong.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})"

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]


# 按年龄排序
sorted_people = sorted(people, key=lambda person: person.age)
print(sorted_people)  # 输出: [Bob (25), Alice (30), Charlie (35)]