# Exception Handling in Python

# There are two types of exceptions in Python:
# 1. SyntaxError
# 2. RuntimeError

# try, except, else, finally

'''
try block is used to handle the exception.
The try block lets you test the code for errors.

If the code contains any error, the except block is executed.
The else block is executed if there is no error.

'finally' block is always executed.

syntax of try block:
try:
    code

except Exception as e:
    code

else:
    code

finally:
    code

When there is no error in our program while using try catch then else block is executed.
When there is any error in our program while using try catch then except block is executed.

'''

# try:
#     print(1/0)

# except Exception as e:
#     print(e)

# else:
#     print("No error")

# finally:
#     print("This is always executed")


# In python we have following exceptions:
# 1. ValueError
# 2. TypeError
# 3. NameError
# 4. IndexError
# 5. KeyError
# 6. AttributeError
# 7. IOError
# 8. ImportError
# 9. SyntaxError
# 10. IndentationError
# 11. RuntimeError
# 12. RecursionError
# 13. AssertionError
# 14. Warning
# 15. UserWarning
# 16. DeprecationWarning
# 17. SyntaxWarning
# 18. RuntimeWarning
# 19. FutureWarning
# 20. PendingDeprecationWarning
# 21. ImportWarning
# 22. UnicodeWarning
# 23. BytesWarning
# 24. ResourceWarning
# 25. OverflowWarning
# 26. RecursionError





# try:
#     print(a)

# except ValueError as e:
#     print(e)

# except NameError as e:
#     print(e)


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# try:
#     print(a/b)

# except Exception as e:
#     print("Exception -> ", e)

# except ZeroDivisionError as e:
#     print("ZeroDivisionError -> ", e)

# In Python code will get executed from top to bottom.

# The raise keyword is used to raise an exception.

# x = int(input("Enter a: "))

# try:
#     if x < 0:
#         raise ValueError("x is less than 0")
#     elif x == 0:
#         raise ZeroDivisionError("x is 0")
#     else:
#         print(x)

# except Exception as e:
#     print(e)

# name = input("Enter your name: ")

# try:
#     if name == "Niraj" or name == "niraj":
#         raise ValueError(f"{name} is not an Employee at this company")
#     else:
#         print(name, "is an Employee at this company")

# except Exception as e:
#     print("Exeception occurred, now im in except block")
#     print(e)

# try:
#     import abcd

# except Exception as e:
#     print(e)

'''
Task-:

1. Print the sum till user given number and if user enters any negative nuber the raise exception.
2. Ask user to enter a number and if user enters any negative number then raise exception.
3. Ask user for a string in Block letters and if user enters any character in lower case then raise exception with a custom message.
4. Ask user for a string and if there is any number in it then raise exception with a custom message.
5. Ask user for any number and if user enter any special symbol or character then raise exception with a custom message(messages will be different for special symbols and characters).

'''