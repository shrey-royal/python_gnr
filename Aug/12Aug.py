# we will use the abc module and from this abc module we will import th ABC class
# ABC class is know and abstract class

from abc import ABC, abstractmethod

# ABC stands for Abstract Base Class

class Car(ABC): # abstract class
    @abstractmethod 
    def drive(self):
        print("This is a normal method")
    
    def mileage(self):
        print("This is a abstract method")
    

class BMW(Car):
    def mileage(self):
        print("BMW mileage is 12kmpl")

class Honda(Car):
    def mileage(self):
        print("Honda mileage is 16kmpl")

class Maruti(Car):
    def mileage(self):
        print("Maruti mileage is 40kmpl")

class Suzuki(Car):
    def mileage(self):
        print("Suzuki mileage is 40kmpl")

class Ford(Car):
    def mileage(self):
        print("Ford mileage is 45kmpl")

class Toyota(Car):
    def mileage(self):
        print("Toyota mileage is 15kmpl")


BMW().mileage()
Honda().mileage()
Maruti().mileage()
Suzuki().mileage()
Ford().mileage()
Toyota().mileage()


# __ -> private
# _ -> protected
# self. -> public