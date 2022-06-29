'''
# Functions - Assistants

# -> Functions are the code that we can write once and use multiple times

# 4 types of functions

-> without arguments and without return type
-> with arguments and without return type
-> without arguments and with return type
-> with arguments and with return type

-> Function provides us Modularity in code
-> Easy Maintability and Debugging in the code

basic syntax of function-: 

def function_name(arguments (optional) ):
    code
    return type (optional)

'''

"""
# 1. without arguments and without return type

# declaration / Definition
def function_1():
    print("This is a Function without arguments and without Return type")

# calling of a function
function_1()

# 2. with arguments and without return type
def function_2(a, b):
    print(a+b)

function_2(2, 3)

# 3. without arguments and with return type
def function_3():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return (a+b)

print(function_3())

# with arguments and with return type
def function_4(a, b):
    return (a+b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(function_4(a, b))

"""

def addString(a, b):
    print(a+b)

addString("a", 's')

# Task-:
# Make a python program to make Calculator using functions
# Take 5 input from the user and calculate and print average using function