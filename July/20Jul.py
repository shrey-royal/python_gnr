'''
# Lambda Function

# normal function have multiple line of code where as a lambda function can only have 1 line

def power(base, p): return base**p # this function is called lambda function

print(power(2, 4))

'''
"""
# *args and **kwargs

arguments -> 2 types of arguments

1. positional arguments

# print(f"{a} is greater than {b}")
print("{0} is greater than {1}".format(12, 2))

2. named arguments -> we will define the values to the variables at the time of definition

print(f"{0} is greater than {1}".format(a = 12, b = 2))

"""

# print("{0} is greater than {1}".format(12, 2))

# *args -> it will taken number of arguments at a time

def printing_numbers(*d):
    print(*d)
    # print(*args)

printing_numbers(1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

printing_numbers(23, numbers, "shrey kadia")


# Task-: Ask user for a number, then scan that many numbers, then print fatorials of that numbers using *args in python.

