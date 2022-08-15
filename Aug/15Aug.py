# args(Non-Keyword arguments) and kwargs(Keyword arguments)

def add(a, b):
    return a + b

def sum(*args):
    sum=0
    for i in args:
        sum+=i

    return sum

    # approach 2
    # return sum(args)

# print("Addition of two numbers:", add(10, 20))

# print("Sum of numbers:", sum(10, 20, 30, 40, 50, 10))

# kwargs -> keyword arguments

def employee(**data):
    print(data)
    print(type(data))
    print(data["name"])
    print(data["age"])
    print(data["salary"])
    print(data["designation"])
    print(data["experience"])
    print(data["address"])
    print(data["phone"])
    print(data["email"])

employee(name="John", age=30, salary=25000, designation="Manager", experience=5, address="Bangalore", phone=9876543210, email="abc@gmail.com")

'''
Task-: 

1. Create a function that takes n number of arguments and return the following things:
    a. Sum of all the arguments
    b. Maximum of all the arguments
    c. Minimum of all the arguments
    d. Average of all the arguments
    e. Concatenation of all the arguments

2. Create a function company() that takes name, address, phone, email as arguments and return the following things:

    a. Name of the company
    b. Address of the company
    c. Phone of the company
    d. Email of the company
    e. number of employees
    f. name of the CEO
    g. name of the CTO
    h. type of the company
    i. product of the company
    j. services of the company
    k. website of the company

'''