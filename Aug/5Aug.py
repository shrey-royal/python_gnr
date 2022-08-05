#types of inhertance:
#1. single level inheritance
# -> One class inherits from another class.

#2. multi level inheritance
# -> One class inherits from another class which inherits from another class.

# 1<-2<-3<-4<-....<-n


#3. hybrid inheritance
#4. multiple inheritance
#5. Hierarchical inheritance




#2. multi level inheritance
# -> One class inherits from another class which inherits from another class.

class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(B):
    def showC(self):
        print("C")

c = C()

c.showA()
c.showB()
c.showC()

'''
Task -: 

    1. Create a class called Shape. It should have a method called area.
    2. Create two classes called Rectangle and Square. 
    3. Square class will inherit Rectangle class.
    4. Rectangle class will inherit Shape class.


    -> Create a class called Animal that has a method called eat.
    -> Create a class called Dog that inherits Animal and has a method called bark, sleep.
    -> Create a class called Snake that inherits Dog and has a method called eat.

'''