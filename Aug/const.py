class Employee():
    def __init__(self, id, name, salary, job_role):
        self.id = id
        self.name = name
        self.salary = salary
        self.job_role = job_role


    def print_employee_details(self):
        print("\nId -> ", self.id)
        print("\nName -> ", self.name)
        print("\nSalary -> ", self.salary)
        print("\nJob Role -> ", self.job_role)


e = Employee(int(input("Enter Id: ")), input("Enter Name: "), float(input("Enter Salary: ")), input("Enter Job Role: "))

e.print_employee_details()



print(getattr(e, "name"))

setattr(e, "salary", 1000000000)

e.print_employee_details()


'''
class has built-in functions

//getters and setter in java

here in python we have

1. getattr(obj, name, default) ->  used to access the attr of object
2. setattr(obj, name, default) -> used to set the attr of object
3. delattr(obj, name) -> used to del the specified attr of any obj
4. hasattr(obj, name) -> used to check if the attr belongs to any obj or not



Task -: 

Create a class called Student containing the attributes like (roll no, name, standard/class, division, medium, name_of_school, age, gender, fees, address, father's name, mother's name, father's number, mother's number).

now ask user for the above mentioned details, and print the details


now you have to ask for the following things form the user

1. see the details
2. change students details

Scan at least 5 student details





'''