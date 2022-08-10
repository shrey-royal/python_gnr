'''

super()


inheritance methods -> 

isinstance() -> it will check whether the given object is the instance of the given class or not.

-> isinstance(obj, class)

issubclass() -> it will check whether the given class is a subclass of the given class or not.

-> issubclass(child_class, parent_class)

'''

# super() -> immediate parent class -> point

# class A:
#     def print_a(self):
#         print("A")

# class B(A):
#     def print_B(self):
#         super().print_a()   # super() -> here super will give the reference of immediate parent class

# class C:
#     def print_C(self):
#         print("C")

# b = B()

# b.print_B()

# c = C()

# print(isinstance(b, A))
# print(issubclass(C, A))

'''

# Polymorphism -> it is a way to use the same method in different classes.
# Method Overriding -> we can give the specific implementation of the method in the child class.

class RBI():
    def RateOfInterest(self):   # original method
        print("Rate of Interest is 8%")

class SBI(RBI):
    def RateOfInterest(self):   # overriding method
        print("ROI is 10%")

class ICICI(RBI):
    def RateOfInterest(self):   # overriding method
        print("Rate of Interest is 12%")

class HDFC(RBI):
    def RateOfInterest(self):   # overriding method
        print("Rate of Interest is 14%")

rbi = RBI()
sbi = SBI()
icici = ICICI()
hdfc = HDFC()

rbi.RateOfInterest()
sbi.RateOfInterest()
icici.RateOfInterest()
hdfc.RateOfInterest()
'''

# method overloading -> we can give the same method with different implementation in the child class.
class Calculator():    
    def add(self, a, b, c=0):   # method is overloaded
        return a + b + c

    def add_str(self, a="\0", b="\0", c="\0", d="\0"):   # method is overloaded
        return a + b + c + d

c = Calculator()

print(c.add(10, 20))    #-> this is not possible because we have already defined the add method in the class.
print(c.add(10, 20, 30))

print(c.add_str("Hello ", "World", "!"))
print(c.add_str())
print("fin.")


'''
Tasks of method overloading-:

class Calculator():
1. Make a method which can add two numbers, two strings and two lists.
2. Make a method which combines all the following things:
    a. Concat two numbers
    b. Concat two strings
    c. Concat two lists

3. User will or will not enter his/her name while calling the method, so u have to handle this.

Output:
scenario 1:
    Enter your name: Shrey K
    Hello Shrey K, how are you?

scenario 2:
    Enter your name: 
    Hello, how are you?

Tasks of method overriding-:

1. Create a class called Calculator which has the following methods:
    a. Add method which can add two numbers
    b. Sub method which can subtract two numbers
    c. Multiply method which can multiply two numbers
    d. Divide method which can divide two numbers
    e. Floor Division method which can give the floor division of two numbers
    f. Power method which can raise one number to the power of another number
    g. Square method which can give the square of a number
    h. Cube method which can give the cube of a number

2. create another class called subCalculator which has the following methods:
    a. Add method which can add three numbers
    b. Sub method which can subtract three numbers
    c. Multiply method which can multiply three numbers
    d. Divide method which can divide three numbers
    e. Floor Division method which can give the floor division of three numbers

print the result of the above operations.


'''