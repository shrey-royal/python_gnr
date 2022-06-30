# Recursion -: It is a method to call same function.
# The process in which a function calls itself directly or indirectly is called recursion

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


print("Fibonacci Series...")
n = int(input("\nEnter how many numbers you want in the series? \n->"))

if (n <= 0):
    print("Please enter a +ve number")
else:
    print("printing fibonacci series...")
    print("0")
    for i in range(n-1):
        print(fibonacci(i))