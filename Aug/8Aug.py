# Inheritance -> 5 types
'''
1. Single level inheritance - 1 base class and 1 derived class
2. Multi level inheritance - 1 base class and 1 child derived classes (chain of inheritance)
3. Hierarchical inheritance - 1 base classes and multiple derived class
4. Mutiple inheritance - multiple base classes and 1 derived class
5. Hybrid inheritance - multiple base classes and multiple derived classes

'''

"""
# Hierarchical inheritance

class Animal():
    def eat(self):
        print("Animal is Eating")

    def sleep(self):
        print("Animal is Sleeping")

class Dog(Animal):
    def bark(self):
        print("Dog is Barking")

class Cat(Animal):
    def meow(self):
        print("Cat is Meowing")

class Parrot(Animal):
    def fly(self):
        print("Parrot is Flying")

print("\n")
dog = Dog()
dog.eat()
dog.bark()
dog.sleep()

print("\n")
cat = Cat()
cat.eat()
cat.meow()
cat.sleep()

print("\n")
parrot = Parrot()
parrot.eat()
parrot.fly()
parrot.sleep()

"""

"""
# multiple Inheritance

class Father():
    def roti(self):
        print("Father is providing roti")

    def kapda(self):
        print("Father is providing kapda")

    def makaan(self):
        print("Father is providing makaan")

class Mother():
    def cooking(self):
        print("Mother is cooking food")

    def shopping(self):
        print("Mother is shopping")

    def cleaning(self):
        print("Mother is cleaning")

class Child(Father, Mother):  # multiple inheritance
    def eating(self):
        print("Son is eating")

    def sleeping(self):
        print("Son is sleeping")

print("\n")
child = Child()
child.eating()
child.sleeping()
child.roti()
child.kapda()
child.makaan()
child.cooking()
child.shopping()
child.cleaning()

"""

# Hybrid Inheritance - complexity -> increase

class Dada():
    def name_of_class1(self):
        print("Dada")

class Dadi(Dada):
    def name_of_class2(self):
        print("Dadi")

class Father(Dadi):   # ambiguous inheritance
    def name_of_class3(self):
        print("Father")

class Mother():
    def name_of_class4(self):
        print("Mother")

class Child(Father, Mother):    # ambiguous inheritance
    def name_of_class5(self):
        print("Child")


print("\n")
child = Child()
child.name_of_class1()
child.name_of_class2()
child.name_of_class3()
child.name_of_class4()
child.name_of_class5()


'''
-> if we see the first 2 classes then they are showing single inheritance
-> if we see the first 3 classes then they are showing multilevel inheritance
-> if we see the last 3 classes then they are showing multiple inheritance
'''

"""
Task-:
1. Create a class called Company and have it have the following properties:
    a. Name of the company
    b. Number of employees
    c. Location of the company
    d. Is the company is a startup or a corporation

2. Create a class called Employee and have it have the following properties:
    a. Name of the employee
    b. Age of the employee
    c. Salary of the employee
    d. Address of the employee
    d. Job Role of the employee

3. Create a class called Product and have it have the following properties:
    a. Name of the product
    b. Price of the product
    c. Brand of the product
    d. Type of the product

4. Create a class called Customer and have it have the following properties:
    a. Name of the customer
    b. Age of the customer
    c. Address of the customer
    d. Number of orders the customer has ordered
    e. Order details of the customer -> product class


# You have to use all 5 types of inheritance in the above classes
"""