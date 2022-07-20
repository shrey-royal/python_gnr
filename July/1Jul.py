# copy a function
"""
def function():
    # return 34
    print("I'm Function")


# print(function())
function()
func2 = function()

func2
print(type(function()))
print(type(func2)) # returns NoneType
"""

# Lambda Function
def lfun(n): return n ** 10 # -> lambda function
print(lfun(2))

def printing(): print("this is a Lambda Function")
printing()

x = lambda n:  (n ** 10)
print(x(2))

y = lambda a, b: print("this is a lambda function using the lambda keyword")
y(1, 2)

'''
SUMMARY : 

# we have 2 types of copies in python
1. shallow copy
2. deep copy

a = 56

b = a   -> shallow copy
# here both a and b are pointing to the same memory location. this type of copy is called shallow copy, here data will not be copied from a to b.

list1 = []

list2 = list1.copy() -> deep copy
# here both the lists are have their own memory locations and the data will be copied from list1 to list2


# here in functions we have shallow copy


-> there is one type of function which have only one line...

# in python it is called Lambda Function

def function_name(arguments): return data / one expression

syntax-: 
lambda arguments: expression

'''