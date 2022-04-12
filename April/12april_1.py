a = 4j  # sqrt(-1)
print(a, type(a))
A = 3
print(A, type(A), sep="\t")
print(id(A))
A = "string"
print(id(A))

a = 2
b = 5
print(a+b)
"""
print("Enter int_1: ")
int_1 = input()
print("Enter int_2: ")
int_2 = input() # input() returns a string

print(type(int_1), type(int_2))
print("Addition: ", int_1 + int_2)
"""

print("Enter int_1: ")
int_1 = float(input())
print("Enter int_2: ")
int_2 = int(input()) # int(input()) returns an int

print(type(int_1), type(int_2))
print("Addition: ", int_1 + int_2)