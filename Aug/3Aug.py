# OOPS concepts -> Interitance

# Inheritance is a way to create new classes based on existing classes.
# This way we can reuse the code in the existing class and modify it as per our need.

'''
terms -: 

superclass, Baseclass -: Parent class
subclass, DerivedClass -: Child class

'''



class Animal(): # Base class
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

    def eat(self):
        print("Animal is Eating")

    def sleep(self):
        print("Animal is Sleeping")

class Dog(Animal):  # Dog is a subclass of Animal and Animal is a superclass of Dog
    def bark(self):
        print("Dog is Barking")

d = Dog("Tommy", 2, "Black", "Labrador")

d.eat()
d.sleep()
d.bark()


"""
Task -: 
create a base class called Animal
create a subclass called Dog
you have to creat at least 10 attributes and 5 methods in both classes


"""