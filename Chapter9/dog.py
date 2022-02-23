# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月14日
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog('Whillie', 6)
your_dog=Dog('Lucy',3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()