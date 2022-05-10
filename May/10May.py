# veg = ['carrot', 'cabbage', 'lettuce', 'tomato', 'potato']
# print(veg)

# print(veg[2:4])

# # numbers = [1, 2, 3, 4, 5]
# # number1 = 7

# # if number1 not in numbers:
# #     print('True')
# # else:
# #     print('False')

# numbers = [1, 2, 3, 4, 5]
# numbers1 = [1, 2, 3, 4, 5]

# print(id(numbers))
# print(id(numbers1))
# num = numbers

# num1 = 1.2
# num2 = 1.2
# num3 = 1

# print(id(num1))
# print(id(num2))
# print(id(num3))


# # if the objects are same or not
# if num1 is num2 is num3:
#     print('True')
# else:
#     print('False')

veg = ['carrot', 'cabbage', 'lettuce', 'tomato', 'potato']

# user supermarket
user_input = input('Enter the vegtable: ')

if user_input in veg:
    print(f"{user_input} is available")
else:
    print(f"{user_input} Out of Stock")

'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence
'''



# if statment
'''
syntax-: 
if condition:
    statement

operators -: 

Arithmetic - // (floor division), ** (power/exponent), / (nearest integer)

print(5/2)  --> 2.5 (return the exact answer)
print(5//2) --> 2   (return the whole number)
print(5**2) (5^2) --> 25  (return the power)

logical
assignment
comparison
bitwise

Membership -> in, not in


ex-: 
if true:
    print('True')

numbers = [1, 2, 3, 4, 5]
number1 = 1

if number1 in numbers:
    print('True')
else:
    print('False')



identity -> is, is not

numbers = [1, 2, 3, 4, 5]
number1 = 1

if number1 is numbers:
    print('True')
else:
    print('False')

'''

