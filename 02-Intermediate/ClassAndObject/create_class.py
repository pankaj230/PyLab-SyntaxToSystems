class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def my_method(self):
        print('This is a test method')

student=Student('pk', 24)
student.my_method()
print(student.name)
print(student.age)


class Bike:
    name='pulsar'
    model='bajaj'

bike=Bike()
print(bike.name)
print(bike.model)


#one more Example
class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def bark(self):
        print(f'{self.name} is {self.age} years old and barking now')

my_dog=Dog('Jakie', 5)
my_dog.bark()
