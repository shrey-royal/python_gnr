# Data Encapsulation

class Person:   # data is wrapped in a class
    
    __name = None
    __age = 0
    __gender = None

    # getters
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    # setters
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setGender(self, gender):
        self.__gender = gender

    # printing details of the person
    def printDetails(self):
        print("Name: ", self.getName())
        print("Age: ", self.getAge())
        print("Gender: ", self.getGender())


# Driver Code
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("1. Male\n2. Female\n3. Prefer not to say")
temp = int(input("Select your gender: "))

if temp == 1:
    gender = "Male"
elif temp == 2:
    gender = "Female"
elif temp == 3:
    gender = "Prefer not to say"

p = Person()

p.setName(name)
p.setAge(age)
p.setGender(gender)

p.printDetails()

# print("age: ", p.getAge())


'''
Task -: 

1. Create a class Called Employee that has the following attributes:
    a. Name
    b. salary
    c. project

2. Create getters and setters method for all the attributes.

3. Create a method called show() that prints the details(name, salary) of the employee.
4. create a method called project() that prints the name of the project that the employee is working on.

'''