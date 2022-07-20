def fact_5():
    def fact(num):
        if num == 1:
            return 1
        
        return num*fact(num-1)
    print((fact(5) + fact(4) + fact(3) + fact(2) + fact(1))/5)

fact_5()


'''
1. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

2. Make a function to check whether the number in argument is prime number or not. Make a supporting Python main program that uses this function to store all the prime numbers in the given range in a dictionary according to their serial number. for example, prime number between range 0 to 15 will be stored in a dictionary as:{1:2, 2:3, 3:5, 4:7, 5:11, 6:13}

'''