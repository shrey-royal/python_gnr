# misc topic of functions
"""
# doc strings -> document string -> manual for that function

# print("to print something")

# 2 ways to print doc string

# __doc__ -> help to print the documentation part of that function

# print(pow.__doc__)

# help(pow)


# we will make our own docstring in any function

# doctstrings are written after the declaration of that function

# def fun():
#     # "" "this is a sample doc string " ""
#     # print("3456789")
#     '''This is a sample doc string in '(single quotes) '''
#     return None


# print(fun.__doc__)
# help(fun)
"""
# recursion -> to call itself again and again

# factorial -> 5! --> 5x4x3x2x1 = 120

# def factorial(num):
#     """This function will return the factorial of given number"""
#     if num == 1:
#         return 1

#     return num*factorial(num-1) # -> recursive step

# print(factorial.__doc__)
# help(factorial)

# call another function from some user defined function
# def func():
#     return print

# func()("printed this string using another function")

# function returning a condition

# def greater5(num):
#     return num > 5

# list1 = [x for x in range(1, 11)]

# print(list1)
# for i in list1:
#     print(greater5(i))

# examples -> 2 days

# Task:- Make a python program that takes input from the user and print the average of fatorials