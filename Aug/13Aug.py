# __ -> private
# _ -> protected
# self. -> public

'''
Access Specifiers in python are used to restrict the access to the members of a class.

There are three types of access specifiers in python:
1. Public (All Classes) - This is the default access specifier. It is used to provide access to all the members of a class.

2. Protected (Inherited Classes) - This access specifier is used to provide access to the members of a class that are intended to be used by derived classes.

3. Private (Within the Class) - This access specifier is used to provide access to the members of a class that are intended to be used only by the class itself.

'''

class Employee:

    _name = None   # protected attribute
    __age = None    # private attribute
    __salary = None # private attribute

    def Scan(self, name, age, salary):
        self._name = name
        self.__age = age
        self.__salary = salary

    def DisplayDetails(self):
        print("Name: ", self._name)
        print("Age: ", self.__age)
        print("Salary: ", self.__salary)

class Intern(Employee):
    def AccessEmployeeDetails(self):
        print("Name: ", self._name)
        # print("Salary: ", self.__salary)

# emp = Employee()

# emp.Scan("John", 25, 10000)

# emp.DisplayDetails()
# print(emp.__age)

i = Intern()

i.Scan("John", 25, 10000)
i.DisplayDetails()
i.AccessEmployeeDetails()


"""
Task on Access Specifiers / Access Modifiers-:
1. Create a class called Employee that has the following members:
    a. Name
    b. Age
    c. Salary
    d. Address
    e. PhoneNumber
    f. Email
    g. Designation
    h. Department

    i. Create a constructor that initializes the members of the class.
    ii. Create a method called DisplayDetails that displays the details of the employee.

2. Create a class called Manager that inherits the members of the Employee class.
    a. Create a method called CalculateYearlySalary that calculates the salary of the manager.

3. Create a class called Intern that inherits the members of the Employee class.
    a. Create a method called GetEmployeeName that returns the name of the employee.
    b. Create a method called GetEmployeeEmail that returns the email of the employee.

"""