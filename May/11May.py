'''
Q. what are loops?
A. Loops executes some piece of code multiple times until some condition is satisfied.

there are 2 categories of loops
1. Entry Controlled Loops --> for loop, while loop
--> conditions are checked at the entry time...

2. Exit Controlled Loops --> do while loop
--> conditions are checked at the exit time...

NOTE-: now python does not have exit controlled loops.

Syntax-: 
    for(initialization; condition; increment/decrement){
        //code to be executed
    }

    for(int i=0; i<10; i++){
        print(i)
    }

    i is the iterator variable
    range is a built-in function that returns a list of numbers
    range(start, end, step)

    for i in range(10):
        print(i)


'''

from distutils import file_util
from tkinter.tix import DisplayStyle


for i in range(1, 10):
    print(i)    # 0 to 9


fruits =['banana', 'apple', 'orange', 'pineapple', 'strawberry', 'grapes']

#using for loop we can traverse lists, strings, tuples, dictionaries, etc.

print(fruits)

# for i in fruits:
#     print(i)

for i in fruits:
    if i == 'pineapple':
        print(f"found fineapple at {fruits.index(i)} index")

# if(condition){
#     //
# }

if 1:
    pass

#make a program that scans age from the user and print if they are eligible to vote or not

# age = int(input('Enter your age: '))

# if age>=18 and age<=110:
#     print("you're eligible to vote")
# else:
    # print("you're not eligible to vote")

#marksheet

# marks = int(input('enter your marks: '))

# if marks>75 and marks<=100:
#     print("Distinction")
# elif marks>60 and marks<=75:
#     print("A Grade")
# else:
#     print("Fail")

# number = int(input('Enter any number: '))

# #shorthand notation for if
# print(f"{number} is positive") if number>0 else print(f"{number} is negetive")

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

print(f"n1 = {n1}, n2 = {n2}")

n1, n2 = n2, n1

print(f"n1 = {n1}, n2 = {n2}")


'''
Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.


    If anyone of you are having any difficulty in understanding the above programs, please feel free to ask me.

    and if you can't able to solve any of the above program, then tell me i'll help you solve it.

    You have time till this friday 6:00 AM.
    
'''