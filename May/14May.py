# while loop programs
"""
# Wap to find the factorial of a given number

# n * n-1 ==> n = 1

num = int(input("Enter any number: "))  # 5 = 5*4*3*2*1

i = 1   #iterator variable
f = 1   #variable that counts factorial
while i <= num: # 6<=5 --> false
    f *= i      # 24 * 5 = 120
    i+=1        # 6

# F-String
# print(f"factorial of {num} is {f}")
print("factorial of {} is {}".format(num, f))
"""
'''
# wap to check whether the num is armstrong or not

digits = 3
153 = 1*1*1 + 5*5*5 + 3*3*3

num = int(input('Enter any number: '))

temp = num
sum = 0
while temp>0:    # num = 153 --> 3 strore temp variable
    digit = temp % 10   # get the last digit from the number
    sum += pow(digit, 3)
    temp //= 10

print(f'{num} is armstrong') if sum == num else print(f'{num} is not an armstrong number')
'''
"""
# wap to check whether the number is palindrome or not

# 1221
# 112211

num = int(input('Enter any number: '))

temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = (rev*10) + digit
    temp //= 10

print(f'{num} is palindrome') if num == rev else print(f'{num} is not a palindrome')
"""
'''
# wap to print the sum of odd numbers between a range(user defined)

# In python switch case is not exist
# it's complexity, the debugging process is hard

start = int(input('Enter start: '))
end = int(input('Enter end: '))

sum = 0
while start<=end:
    if start%2 != 0:
        sum += start    
    start += 1

print(f'{sum} is the answer')
'''


# WAP to find the no. of digits in the given number

# num = int(input('Enter any number: '))
# num1 = num
# digit_counter = 0
# while num > 0:
#     num //= 10
#     # print(num)
#     digit_counter+=1
# print(f'{num1} have {digit_counter} digits')



'''
# u can use while loop, for loop.
1. 
*
**
***
****


2. 
1
12
123
1234


3. 
1
2 3
4 5 6
7 8 9 10

4. 
1
22
333
4444

5. 
1234
123
12
1

6. 
1234
234
34
4

7. 
4321
321
21
1

8. 
4
43
432
4321

9. 
12345
 1234
  123
   12
    1

10.
     *
    ***
   *****
  *******


11.

A
AB
ABC
ABCD
ABCDE

12. 
1234321
12   21
1     1
12   21
1234321


13. 
  1
 121
12321


//9, 12, 13

'''
"""
# 9. 
# 12345
#  1234
#   123
#    12
#     1

num = int(input('Enter any number: '))

for i in range(1, num+1):
    k=1
    for j in range(1, num+2):
        if j<=i:
            print(' ', end="")
        else:
            print(k, end="")
            k+=1
    print()

"""
'''
# 12. 
# 1234321
# 12   21
# 1     1
# 12   21
# 1234321


'''

# 13. 
#   1
#  121
# 12321



